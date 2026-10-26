#!/usr/bin/env python3
"""Attach semantic_digital_twin annotations to the articulated objects.

Planning (which link gets which annotation) uses the standard library only and reads
``collection.json`` and each ``model.urdf``. Applying the plan needs the
``semantic_digital_twin`` package of cognitive_robot_abstract_machine:

    ~/venvs/cram-env/bin/python scripts/annotate_semantics.py            # all objects
    ~/venvs/cram-env/bin/python scripts/annotate_semantics.py 033 001    # some objects
    python3 scripts/annotate_semantics.py --plan-only --json plan.json   # no SDT needed

Other code can call ``load_annotated_world(folder)`` to get an annotated World.

``--write-semantics`` stores the result as ``semantics.json`` in every object folder, so
the annotations can be read without running anything; regenerate it after changing a
model or the rules below. The groups above the categories come from ``group`` in
``collection.json``; the class for each object type comes from ``semantic_concepts.json``,
which ``scripts/sync_semantics.py`` keeps in step with cram2.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional

SOURCE = Path(__file__).resolve().parents[1] / "objects" / "articulated"

CONCEPTS_FILE = SOURCE / "semantic_concepts.json"
AVAILABLE = "available"


def read_concepts(path: Path = CONCEPTS_FILE) -> dict:
    """The concept registry: which class each object type should get, and whether cram2
    has it. ``scripts/sync_semantics.py`` keeps it in step with cram2."""
    return json.loads(path.read_text(encoding="utf-8"))


CONCEPTS = read_concepts()
FALLBACK_ROOT_CLASS = CONCEPTS["fallback"]

# Words in a moving link's name that make it a door or a drawer. The last of these
# words in the name decides, so ``right_door_handle`` and ``left_door_lever`` are
# controls on a door, not doors.
DOOR_WORDS = {"door", "flap", "lid", "cover", "gate"}
DRAWER_WORDS = {"drawer", "basket", "bin", "tray", "pullout", "bucket", "rack", "crate",
                "box", "shelf", "compartment"}
TILTING_DRAWER_WORDS = {"drawer", "bin", "compartment"}
OTHER_WORDS = {"handle", "lever", "knob", "button", "latch", "switch", "dial", "lock"}
MOVING = {"revolute", "prismatic", "continuous"}


@dataclass
class PlannedAnnotation:
    link: str
    annotation: str
    description: Optional[str] = None
    type_description: Optional[str] = None
    concept: Optional[str] = None
    """The class the link should have once cram2 provides it, when ``annotation`` is the
    fallback in its place."""


def root_class(object_type: str, concepts: dict = CONCEPTS) -> tuple[str, Optional[str]]:
    """The class to annotate an object's root with, and the concept it stands in for.

    :return: ``(concept, None)`` when cram2 has a usable class for the object's type,
        otherwise ``(fallback, concept)``, with ``concept`` None for types no concept
        is assigned to.
    """
    concept = concepts["object_types"].get(object_type)
    if concept is not None and concepts["concepts"][concept]["cram"] == AVAILABLE:
        return concept, None
    return concepts["fallback"], concept


def name_words(link: str, slug: str) -> list[str]:
    """The words of a link name after the object slug, e.g. ``bin_r1c1`` -> bin, r1c1."""
    name = link[len(slug) + 1:] if link.startswith(slug + "_") else link
    return name.split("_")


def moving_part_class(words: list[str], joint_type: str) -> str:
    vocabulary = DOOR_WORDS | DRAWER_WORDS | OTHER_WORDS
    stems = [re.sub(r"\d+", "", w) for w in words]
    word = next((w for w in reversed(stems) if w in vocabulary), None)
    if word in DOOR_WORDS and joint_type in {"revolute", "prismatic"}:
        return "Door"
    if word in DRAWER_WORDS and (joint_type == "prismatic" or
                                 (joint_type == "revolute" and word in TILTING_DRAWER_WORDS)):
        return "Drawer"
    return "NaturalLanguageDescription"


def plan_object(obj: dict, source: Path = SOURCE) -> list[PlannedAnnotation]:
    """Annotations for one collection.json entry, root first, parents before children."""
    robot = ET.parse(source / obj["folder"] / "model.urdf").getroot()
    joints = {j.find("child").get("link"): j.get("type") for j in robot.findall("joint")}
    roots = [link.get("name") for link in robot.findall("link")
             if link.get("name") not in joints]
    if len(roots) != 1:
        raise ValueError(f"{obj['folder']}: expected one root link, found {roots}")
    object_type = obj["fingerprint"]["type"]
    cls, concept = root_class(object_type)
    fallback = cls == FALLBACK_ROOT_CLASS
    plan = [PlannedAnnotation(roots[0], cls, obj["name"] if fallback else None,
                              object_type if fallback else None, concept)]
    grips = {f["name"] for f in obj["frames"] if f["purpose"] == "grasp"}
    for joint in robot.findall("joint"):
        link, joint_type = joint.find("child").get("link"), joint.get("type")
        if joint_type in MOVING:
            words = name_words(link, obj["slug"])
            cls = moving_part_class(words, joint_type)
            plan.append(PlannedAnnotation(
                link, cls, " ".join(words) if cls == "NaturalLanguageDescription" else None))
        elif link in grips:
            # A grip frame is an empty link placed where a gripper takes hold, which is
            # what coraplex's OpenAction grasps and moves (handle.root).
            plan.append(PlannedAnnotation(link, "Handle"))
    return plan


def read_objects(source: Path = SOURCE) -> list[dict]:
    return json.loads((source / "collection.json").read_text(encoding="utf-8"))["objects"]


# --- applying a plan with semantic_digital_twin ---------------------------------------

def _annotation_classes() -> dict:
    from semantic_digital_twin.semantic_annotations import natural_language, semantic_annotations
    names = {c for c, entry in CONCEPTS["concepts"].items() if entry["cram"] == AVAILABLE}
    names |= {FALLBACK_ROOT_CLASS, "NaturalLanguageDescription", "Door", "Drawer", "Handle"}
    return {n: getattr(semantic_annotations, n, None) or getattr(natural_language, n)
            for n in names}


def _accepting_field(whole, part) -> Optional[str]:
    """The part-whole field of ``whole`` that can still take ``part``, if any."""
    from semantic_digital_twin.semantic_annotations.mixins import HasDoors, HasDrawers, HasHandle
    from semantic_digital_twin.semantic_annotations.semantic_annotations import Door, Drawer, Handle
    if isinstance(part, Handle) and isinstance(whole, HasHandle) and whole.handle is None:
        return "handle"
    if isinstance(part, Door) and isinstance(whole, HasDoors):
        return "doors"
    if isinstance(part, Drawer) and isinstance(whole, HasDrawers):
        return "drawers"
    return None


def apply_plan(world, plan: list[PlannedAnnotation]) -> dict[str, Optional[str]]:
    """Add the planned annotations to ``world`` and link parts to their wholes.

    A part joins the nearest ancestor annotation that can hold it. When that ancestor is
    its direct kinematic parent, ``add`` is used (its mount is then a no-op); otherwise
    the field is set directly, because mounting would re-parent the part and break the
    joints in between (e.g. a grip frame on a door's lever handle).

    :return: For each annotated link, the link of the whole it became part of, or None.
    """
    classes = _annotation_classes()
    by_link, part_of = {}, {}
    with world.modify_world():
        for planned in plan:
            kwargs = {k: v for k, v in (("description", planned.description),
                                        ("type_description", planned.type_description))
                      if v is not None}
            annotation = classes[planned.annotation](
                root=world.get_body_by_name(planned.link), **kwargs)
            world.add_semantic_annotation(annotation)
            by_link[planned.link] = annotation
        by_body = {a.root: a for a in by_link.values()}
        for link, annotation in by_link.items():
            part_of[link] = None
            for depth, ancestor in enumerate(_ancestors(annotation.root)):
                whole = by_body.get(ancestor)
                field = whole is not None and _accepting_field(whole, annotation)
                if not field:
                    continue
                if depth == 0:
                    whole.add(annotation, field_name=field)
                elif field == "handle":
                    whole.handle = annotation
                else:
                    getattr(whole, field).append(annotation)
                part_of[link] = ancestor.name.name
                break
    return part_of


def _ancestors(body):
    while body.parent_connection is not None:
        body = body.parent_connection.parent
        yield body


GRAPH_COLOURS = {"Handle": "#f4c06b", "Door": "#8fc1e3", "Drawer": "#9ad19a",
                 "NaturalLanguageDescription": "#e6e6e6"}
WHOLE_COLOUR, FRAME_COLOUR = "#d7a6e0", "white"


def graph_data(world, obj: Optional[dict] = None) -> dict:
    """The annotated kinematic tree as plain data, shared by the Graphviz and HTML views.

    Nodes are the world's links with their annotation; edges are the joints and, with
    ``part`` set, the part-whole relations from a whole to its doors, drawers and handle.
    ``obj`` (the collection.json entry) adds joint limits and frame purposes.
    """
    joints = {j["name"]: j for j in (obj or {}).get("joints", [])}
    purposes = {f["name"]: f["purpose"] for f in (obj or {}).get("frames", [])}
    annotations = {a.root: a for a in world.semantic_annotations}
    nodes, edges = [], []
    for entity in world.kinematic_structure_entities:
        name, annotation = entity.name.name, annotations.get(entity)
        node = {"id": name, "annotation": type(annotation).__name__ if annotation else None,
                "description": getattr(annotation, "description", None),
                "type_description": getattr(annotation, "type_description", None),
                "purpose": purposes.get(name)}
        connection = entity.parent_connection
        if connection is not None:
            node["joint"] = type(connection).__name__.removesuffix("Connection")
            limits = joints.get(connection.name.name)
            if limits and limits.get("lower") is not None:
                node["limits"] = [limits["lower"], limits["upper"]]
            edges.append({"from": connection.parent.name.name, "to": name,
                          "kind": node["joint"], "part": False})
        nodes.append(node)
    for annotation in annotations.values():
        parts = [*getattr(annotation, "doors", []), *getattr(annotation, "drawers", [])]
        if getattr(annotation, "handle", None) is not None:
            parts.append(annotation.handle)
        edges += [{"from": annotation.root.name.name, "to": part.root.name.name,
                   "kind": "part", "part": True} for part in parts]
    return {"nodes": nodes, "edges": edges}


def annotation_graph(world, title: str = "") -> str:
    """Graphviz source of the kinematic tree, with each body's annotation.

    Solid edges are joints, as in ``World.visualize_world_structure``; dashed edges
    point from a whole to each of its parts (doors, drawers, handle).
    """
    def quote(text):
        return '"' + text.replace('"', '').replace("\n", "\\n") + '"'

    data = graph_data(world)
    lines = ["digraph G {", '  graph [rankdir=TB, fontname="Helvetica", labelloc=t, '
             f'label={quote(title)}];',
             '  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=10];',
             '  edge [fontname="Helvetica", fontsize=8, color="#555555"];']
    for node in data["nodes"]:
        cls = node["annotation"]
        if cls is None:
            lines.append(f'  {quote(node["id"])} [label={quote(node["id"])}, '
                         f'fillcolor="{FRAME_COLOUR}", color="#aaaaaa", fontcolor="#777777"];')
            continue
        text = f"{node['id']}\n«{cls}»"
        if node["description"] and cls != "NaturalLanguageDescription":
            text += f"\n{node['description']}"
        colour = GRAPH_COLOURS.get(cls, WHOLE_COLOUR)
        lines.append(f'  {quote(node["id"])} [label={quote(text)}, fillcolor="{colour}"];')
    for edge in data["edges"]:
        if edge["part"]:
            style = 'style=dashed, color="#b03a9c", fontcolor="#b03a9c", constraint=false'
        else:
            style = "style=dotted" if edge["kind"] == "Fixed" else "style=solid"
        lines.append(f'  {quote(edge["from"])} -> {quote(edge["to"])} '
                     f'[label="{edge["kind"]}", {style}];')
    lines.append("}")
    return "\n".join(lines) + "\n"


HTML_TEMPLATE = Path(__file__).with_name("annotation_graph.html")

SEMANTICS_FILE = "semantics.json"
UNGROUPED = "Other"


def read_categories(source: Path = SOURCE) -> dict[str, dict]:
    """Category key -> its collection.json entry; ``group`` is the group above it."""
    data = json.loads((source / "collection.json").read_text(encoding="utf-8"))
    return {c["key"]: {**c, "group": c.get("group", UNGROUPED)} for c in data["categories"]}


def semantics_document(obj: dict, plan: list[PlannedAnnotation],
                       part_of: dict[str, Optional[str]], categories: dict[str, dict]) -> dict:
    """The ``semantics.json`` of one object folder: its taxonomy and every annotation.

    ``attached_to`` is the link an annotated link hangs from in the URDF; ``part_of`` is
    the whole it belongs to semantically (a door's cabinet, a handle's door), or None
    when no annotation has a part-whole field for it, e.g. a knob.
    """
    from semantic_digital_twin.semantic_annotations import natural_language, semantic_annotations
    robot = ET.parse(SOURCE / obj["folder"] / "model.urdf").getroot()
    parents = {j.find("child").get("link"): j.find("parent").get("link")
               for j in robot.findall("joint")}
    modules = {cls: (semantic_annotations if hasattr(semantic_annotations, cls)
                     else natural_language).__name__
               for cls in sorted({p.annotation for p in plan})}
    category = categories[obj["category"]]
    annotations = []
    for planned in plan:
        item = {"link": planned.link, "annotation": planned.annotation}
        if planned.description is not None:
            item["description"] = planned.description
        if planned.type_description is not None:
            item["type_description"] = planned.type_description
        if planned.concept is not None:
            # the class this link waits for; see semantic_concepts.json for its state in cram2
            item["concept"] = planned.concept
            item["concept_status"] = CONCEPTS["concepts"][planned.concept]["cram"]
        item["attached_to"] = parents.get(planned.link)
        item["part_of"] = part_of[planned.link]
        annotations.append(item)
    return {
        "generator": "scripts/annotate_semantics.py",
        "urdf": "model.urdf",
        "object": {"id": obj["id"], "name": obj["name"], "type": obj["fingerprint"]["type"],
                   "category": obj["category"], "category_title": category["title"],
                   "group": category["group"]},
        "annotation_classes": {cls: f"{module}.{cls}" for cls, module in modules.items()},
        "annotations": annotations,
    }


def write_html(objects: list[dict], path: Path,
               categories: Optional[dict[str, dict]] = None) -> Path:
    """Write one self-contained interactive page for the given objects.

    Each item of ``objects`` is a collection.json entry with its ``graph_data`` under
    ``"graph"``; ``categories`` is ``read_categories()`` unless given.
    The page draws collection -> group -> category -> object above each object's links.
    It loads vis-network (the library krrood's VisNetworkGraphVisualizer uses) from a
    CDN, so viewing it needs internet access.
    """
    if categories is None:
        categories = read_categories()
    unknown = {"group": UNGROUPED}
    payload = [{"id": o["id"], "name": o["name"], "category": o["category"],
                "category_title": categories.get(o["category"], unknown).get("title", o["category"]),
                "group": categories.get(o["category"], unknown)["group"],
                "type": o["fingerprint"]["type"], "graph": o["graph"]} for o in objects]
    page = HTML_TEMPLATE.read_text(encoding="utf-8").replace(
        "/*DATA*/[]", json.dumps(payload, separators=(",", ":")).replace("</", "<\\/"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page, encoding="utf-8")
    return path


def write_graph(world, path: Path, title: str = "") -> Path:
    """Write ``annotation_graph`` as .dot, and as .svg/.png when Graphviz is installed.

    The .dot source of a rendered image goes into a ``dot/`` folder beside it, so a
    folder of images is not interleaved with their sources.
    """
    import shutil
    import subprocess
    rendered = path.suffix != ".dot" and shutil.which("dot")
    dot = (path.parent / "dot" / path.name if rendered else path).with_suffix(".dot")
    dot.parent.mkdir(parents=True, exist_ok=True)
    dot.write_text(annotation_graph(world, title), encoding="utf-8")
    if rendered:
        path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["dot", f"-T{path.suffix[1:]}", str(dot), "-o", str(path)], check=True)
        return path
    return dot


def load_annotated_world(folder: Path, obj: Optional[dict] = None):
    """Parse ``folder/model.urdf`` and attach its semantic annotations."""
    from semantic_digital_twin.adapters.urdf import URDFParser
    folder = Path(folder).resolve()
    if obj is None:
        obj = next(o for o in read_objects() if (SOURCE / o["folder"]).resolve() == folder)
    world = URDFParser.from_file(file_path=str(folder / "model.urdf")).parse()
    apply_plan(world, plan_object(obj))
    return world


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("ids", nargs="*", help="object ids, e.g. 033 (default: all)")
    parser.add_argument("--plan-only", action="store_true",
                        help="only derive the annotations, without semantic_digital_twin")
    parser.add_argument("--json", type=Path, help="write the annotations per object here")
    parser.add_argument("--graph", type=Path, metavar="DIR",
                        help="draw each object's annotations into DIR/<id>-<slug>.<format>")
    parser.add_argument("--graph-format", default="svg", choices=["svg", "png", "pdf", "dot"])
    parser.add_argument("--html", type=Path, metavar="FILE",
                        help="write one interactive graph page for all selected objects")
    parser.add_argument("--write-semantics", action="store_true",
                        help=f"write {SEMANTICS_FILE} into each selected object folder")
    args = parser.parse_args(argv)
    if (args.graph or args.html or args.write_semantics) and args.plan_only:
        parser.error("--graph, --html and --write-semantics need the annotated world, "
                     "not --plan-only")
    graphs, categories = [], read_categories()

    objects = [o for o in read_objects() if not args.ids or o["id"] in args.ids]
    report, totals, failures = {}, Counter(), 0
    if not args.plan_only:
        import logging
        logging.disable(logging.WARNING)
        from semantic_digital_twin.adapters.urdf import URDFParser
        _annotation_classes()  # fail once on a missing dependency, not per object
    for obj in objects:
        plan = plan_object(obj)
        entry = {"folder": obj["folder"], "annotations": [asdict(p) for p in plan]}
        if not args.plan_only:
            try:
                world = URDFParser.from_file(
                    file_path=str((SOURCE / obj["folder"] / "model.urdf").resolve())).parse()
                part_of = apply_plan(world, plan)
            except Exception as error:  # report every object, then fail at the end
                failures += 1
                print(f"{obj['id']} FAILED: {type(error).__name__}: {error}", file=sys.stderr)
                continue
            for item in entry["annotations"]:
                item["part_of"] = part_of[item["link"]]
            if args.graph:
                write_graph(world, args.graph / f"{obj['id']}-{obj['slug']}.{args.graph_format}",
                            f"#{obj['id']} {obj['name']}")
            if args.html:
                graphs.append({**obj, "graph": graph_data(world, obj)})
            if args.write_semantics:
                document = semantics_document(obj, plan, part_of, categories)
                (SOURCE / obj["folder"] / SEMANTICS_FILE).write_text(
                    json.dumps(document, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        counts = Counter(p.annotation for p in plan)
        totals.update(counts)
        report[obj["id"]] = entry
        print(f"{obj['id']} {obj['slug']}: {plan[0].annotation}, "
              + ", ".join(f"{n}x {c}" for c, n in sorted(counts.items())))
    print("total: " + ", ".join(f"{n}x {c}" for c, n in totals.most_common()))
    if args.json:
        args.json.write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8")
    if args.html:
        print(f"interactive graph: {write_html(graphs, args.html, categories)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
