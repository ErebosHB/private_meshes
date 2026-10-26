#!/usr/bin/env python3
"""Keep semantic_concepts.json in step with the annotation classes of cram2.

The registry ``objects/articulated/semantic_concepts.json`` names the class each object
type should be annotated with and whether cram2 has it. This script reads a cram2
checkout without importing it (the class definitions are parsed from source), and for
every difference prepares one small pull request, either for cram2 or for this
repository:

    python3 scripts/sync_semantics.py status  --cram ~/cram2
    python3 scripts/sync_semantics.py prepare --cram ~/cram2 --out semantic-sync

``prepare`` only writes, per pull request, a ``description.md`` (the text reviewers read
on GitHub), a ``steps.md`` (the commands to apply, test, commit and open it) and a
``change.patch`` into ``--out``; it never creates branches, commits or pull requests.
"""
from __future__ import annotations

import argparse
import ast
import difflib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "objects" / "articulated" / "semantic_concepts.json"
COLLECTION = ROOT / "objects" / "articulated" / "collection.json"
PACKAGE = Path("semantic_digital_twin/src/semantic_digital_twin")
MODULE_FILE = PACKAGE / "semantic_annotations" / "semantic_annotations.py"
TEST_DIR = Path("test/semantic_digital_twin_test/test_semantic_annotations")
# A class can annotate a body when it reaches this mixin, which declares ``root``.
ROOT_MIXIN = "HasRootKinematicStructureEntity"
AVAILABLE, MISSING, UNUSABLE = "available", "missing", "unusable"
DECLINED = "declined"
"""A concept cram2 turned down: kept on the fallback and not proposed again, unless cram2
gains the class anyway."""
FOLDER = re.compile(r"\d{2}-(cram2|private_meshes)-[a-z0-9-]+")
# PR.md is what earlier versions wrote, so their folders are cleared too
PREPARED_FILES = {"description.md", "steps.md", "change.patch", "PR.md"}
GENERATE = "~/venvs/cram-env/bin/python scripts/annotate_semantics.py --write-semantics"


# --- reading cram2 ------------------------------------------------------------------------

@dataclass
class CramClasses:
    """The classes of a cram2 checkout, read from its source."""

    root: Path
    bases: dict[str, list[str]] = field(default_factory=dict)
    """Every class in the package, by name, with the names of its bases."""
    annotations: set[str] = field(default_factory=set)
    """The classes defined in the semantic_annotations module itself."""
    module_names: set[str] = field(default_factory=set)
    """Every name the semantic_annotations module defines or imports."""

    @classmethod
    def read(cls, root: Path) -> CramClasses:
        if not (root / MODULE_FILE).is_file():
            raise SystemExit(f"{root} is not a cram2 checkout: {MODULE_FILE} is missing")
        classes = cls(root)
        for file in sorted((root / PACKAGE).rglob("*.py")):
            tree = ast.parse(file.read_text(encoding="utf-8"), str(file))
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    bases = [_name(b) for b in node.bases]
                    # the annotation module's own definition wins over a namesake elsewhere
                    if file == root / MODULE_FILE or node.name not in classes.bases:
                        classes.bases[node.name] = bases
            if file == root / MODULE_FILE:
                for node in tree.body:
                    if isinstance(node, ast.ClassDef):
                        classes.annotations.add(node.name)
                        classes.module_names.add(node.name)
                    elif isinstance(node, (ast.Import, ast.ImportFrom)):
                        classes.module_names |= {a.asname or a.name.split(".")[0] for a in node.names}
        return classes

    def has_root(self, name: str, seen: Optional[set] = None) -> bool:
        seen = seen if seen is not None else set()
        if name == ROOT_MIXIN:
            return True
        if name in seen or name not in self.bases:
            return False
        seen.add(name)
        return any(self.has_root(base, seen) for base in self.bases[name])

    def inherits(self, name: str, ancestor: str, seen: Optional[set] = None) -> bool:
        seen = seen if seen is not None else set()
        if name in seen or name not in self.bases:
            return False
        seen.add(name)
        return any(base == ancestor or self.inherits(base, ancestor, seen)
                   for base in self.bases[name])

    def status(self, concept: str) -> str:
        if concept not in self.annotations:
            return MISSING
        return AVAILABLE if self.has_root(concept) else UNUSABLE

    def commit(self) -> Optional[str]:
        result = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"],
                                capture_output=True, text=True)
        return result.stdout.strip() or None


def _name(node: ast.expr) -> str:
    """The class a base expression names: ``HasRootKinematicStructureEntity[Body]`` and
    ``mixins.HasRootBody`` name ``HasRootKinematicStructureEntity`` and ``HasRootBody``."""
    if isinstance(node, ast.Subscript):
        return _name(node.value)
    return node.attr if isinstance(node, ast.Attribute) else getattr(node, "id", ast.unparse(node))


# --- asking GitHub about pull requests already opened -------------------------------------

PRIVATE_MESHES_REPOSITORY = "sunava/private_meshes"
OPEN, MERGED, CLOSED = "open", "merged", "closed"


@dataclass
class PullRequest:
    url: str
    state: str
    """open, merged, or closed (closed without merging)."""


class GitHubUnavailable(Exception):
    pass


def fork_owner(checkout: Path) -> Optional[str]:
    """The GitHub account of ``origin``, the fork pull requests are opened from."""
    result = subprocess.run(["git", "-C", str(checkout), "remote", "get-url", "origin"],
                            capture_output=True, text=True)
    match = re.search(r"github\.com[:/]([^/]+)/", result.stdout)
    return match.group(1) if match else None


def find_pull_request(repository: str, owner: str, branch: str) -> Optional[PullRequest]:
    """The newest pull request into ``repository`` from ``owner:branch``, if any.

    Uses GitHub's public API; ``GITHUB_TOKEN`` or ``GH_TOKEN`` raise its rate limit."""
    import os
    import urllib.error
    import urllib.parse
    import urllib.request
    query = urllib.parse.urlencode({"state": "all", "head": f"{owner}:{branch}", "per_page": 10})
    request = urllib.request.Request(f"https://api.github.com/repos/{repository}/pulls?{query}",
                                     headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            pulls = json.load(response)
    except (urllib.error.URLError, OSError, ValueError) as error:
        raise GitHubUnavailable(str(error)) from error
    if not pulls:
        return None
    newest = max(pulls, key=lambda p: p["created_at"])
    state = MERGED if newest.get("merged_at") else OPEN if newest["state"] == "open" else CLOSED
    return PullRequest(newest["html_url"], state)


def look_up_pull_requests(changes: list[Change], registry: dict, owners: dict[str, Optional[str]],
                          find=find_pull_request) -> Optional[str]:
    """Attach to each change the pull request already opened for it.

    :param owners: the fork owner per repository side (``cram2``, ``private_meshes``).
    :return: why GitHub could not be asked, or None when it answered.
    """
    targets = {"cram2": registry["cram"]["repository"], "private_meshes": PRIVATE_MESHES_REPOSITORY}
    for change in changes:
        owner = owners.get(change.repository)
        if owner is None:
            return f"no GitHub fork found as origin for {change.repository}"
        try:
            change.pull_request = find(targets[change.repository], owner, change.branch)
        except GitHubUnavailable as error:
            return str(error)
    return None


# --- comparing ----------------------------------------------------------------------------

@dataclass
class Change:
    """One difference between the registry and cram2, and the pull request it needs."""

    kind: str
    """add-class / add-bases (for cram2), adopt / withdraw / map-type (for this repository)."""
    concept: str
    cram_status: str
    objects: list[dict]
    object_type: Optional[str] = None
    pull_request: Optional[PullRequest] = None
    """The pull request GitHub has for this change's branch, if one was opened."""

    @property
    def repository(self) -> str:
        return "cram2" if self.kind in ("add-class", "add-bases") else "private_meshes"

    @property
    def slug(self) -> str:
        words = re.sub(r"(?<!^)(?=[A-Z])", "-", self.concept).lower()
        return f"{self.kind}-{words}"

    @property
    def branch(self) -> str:
        """The branch the pull request is opened from; GitHub is asked about this name."""
        return f"semantics/{self.slug}"


def compare(registry: dict, cram: CramClasses, objects: list[dict]) -> list[Change]:
    by_concept: dict[str, list[dict]] = {}
    for obj in objects:
        concept = registry["object_types"].get(obj["fingerprint"]["type"])
        if concept:
            by_concept.setdefault(concept, []).append(obj)
    changes = []
    for concept, entry in registry["concepts"].items():
        expected, actual = entry["cram"], cram.status(concept)
        proposal = entry.get("proposal", {})
        users = by_concept.get(concept, [])
        if actual == AVAILABLE and expected != AVAILABLE:
            changes.append(Change("adopt", concept, actual, users))
        elif expected == AVAILABLE and actual != AVAILABLE:
            changes.append(Change("withdraw", concept, actual, users))
        elif expected == DECLINED:
            continue
        elif actual == MISSING and "bases" in proposal:
            changes.append(Change("add-class", concept, actual, users))
        elif actual == UNUSABLE and "add_bases" in proposal:
            # subclasses gain the root too, e.g. OfficeChair from Chair
            heirs = [o for c, objs in by_concept.items() if cram.inherits(c, concept) for o in objs]
            changes.append(Change("add-bases", concept, actual, users + heirs))
    # cram2 may already have a class for a type no concept is assigned to yet
    for object_type, users in unassigned_types(registry, objects).items():
        concept = _camel(object_type)
        if concept not in registry["concepts"] and cram.status(concept) == AVAILABLE:
            changes.append(Change("map-type", concept, AVAILABLE, users, object_type))
    return changes


def _camel(object_type: str) -> str:
    return "".join(w.capitalize() for w in re.split(r"[^a-z0-9]+", object_type.lower()) if w)


def unassigned_types(registry: dict, objects: list[dict]) -> dict[str, list[dict]]:
    """Object types the registry says nothing about, with their objects.

    A type mapped to ``null`` is decided: it stays on the fallback on purpose."""
    unassigned: dict[str, list[dict]] = {}
    for obj in objects:
        if obj["fingerprint"]["type"] not in registry["object_types"]:
            unassigned.setdefault(obj["fingerprint"]["type"], []).append(obj)
    return dict(sorted(unassigned.items()))


def similar_concepts(object_type: str, registry: dict, cram: CramClasses) -> list[str]:
    """Concepts and usable cram2 classes sharing a word with the type, as a hint:
    ``dryer`` suggests TumbleDryer, ``sofa bed`` suggests Sofa and Bed."""
    generic = {"machine", "unit", "station", "with"}  # name kinds of thing, not the thing
    words = {w for w in re.split(r"[^a-z0-9]+", object_type.lower()) if len(w) > 2} - generic
    candidates = set(registry["concepts"]) | {c for c in cram.annotations if cram.has_root(c)}
    return sorted(c for c in candidates
                  if words & {t.lower() for t in re.findall(r"[A-Z][a-z0-9]*", c)})


# --- preparing pull requests --------------------------------------------------------------

def _diff(path: Path, before: str, after: str) -> str:
    return "".join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                        f"a/{path.as_posix()}", f"b/{path.as_posix()}"))


def class_source(concept: str, proposal: dict) -> str:
    doc = "\n".join(f"    {line}".rstrip() for line in proposal["doc"])
    source = (f'\n\n@dataclass(eq=False)\nclass {concept}({", ".join(proposal["bases"])}):\n'
              f'    """\n{doc}\n    """\n')
    if proposal.get("hole_direction"):
        source += ("\n    @classproperty\n    def _hole_direction_axis(cls) -> Vector3:\n"
                   f"        return Vector3.{proposal['hole_direction']}()\n")
    return source


def snake(concept: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", concept).lower()


def test_path(concept: str) -> Path:
    # one file per concept, so that pull requests for different concepts never touch the same file
    return TEST_DIR / f"test_private_meshes_{snake(concept)}.py"


def test_source(concept: str) -> str:
    """A test that ``concept`` can annotate a body."""
    return ('"""\nThe private_meshes objects of this kind are annotated with this class.\n"""\n\n'
            "from semantic_digital_twin.datastructures.prefixed_name import PrefixedName\n"
            f"from semantic_digital_twin.semantic_annotations.semantic_annotations import {concept}\n"
            "from semantic_digital_twin.world import World\n"
            "from semantic_digital_twin.world_description.world_entity import Body\n\n\n"
            f"def test_{snake(concept)}_annotates_a_body():\n"
            "    world = World()\n"
            f'    body = Body(name=PrefixedName("{snake(concept)}"))\n'
            "    with world.modify_world():\n"
            "        world.add_kinematic_structure_entity(body)\n"
            f"        annotation = {concept}(root=body)\n"
            "        world.add_semantic_annotation(annotation)\n"
            f"    assert world.get_semantic_annotations_by_type({concept}) == [annotation]\n"
            "    assert annotation.root is body\n")


def _insert_after(module: str, anchor: Optional[str], source: str) -> str:
    """``source`` placed after the definition of class ``anchor``, or at the end.

    A different anchor per concept keeps pull requests for different concepts out of
    each other's way."""
    for node in ast.parse(module).body:
        if isinstance(node, ast.ClassDef) and node.name == anchor:
            lines = module.splitlines(True)
            return "".join(lines[:node.end_lineno]) + source + "".join(lines[node.end_lineno:])
    return module.rstrip("\n") + "\n" + source


def cram_patch(change: Change, entry: dict, cram: CramClasses) -> tuple[str, list[str]]:
    """The patch for cram2, and the warnings a reviewer should see."""
    module = (cram.root / MODULE_FILE).read_text(encoding="utf-8")
    proposal, warnings = entry["proposal"], []
    if change.kind == "add-class":
        bases = proposal["bases"]
        if proposal.get("after") and proposal["after"] not in cram.annotations:
            warnings.append(f"`{proposal['after']}` is gone from cram2; the class goes at the end.")
        after = _insert_after(module, proposal.get("after"), class_source(change.concept, proposal))
    else:
        bases = proposal["add_bases"]
        pattern = re.compile(rf"^class {change.concept}\((.*?)\):", re.M)
        match = pattern.search(module)
        after = pattern.sub(lambda m: f"class {change.concept}({m.group(1)}, {', '.join(bases)}):",
                            module, count=1)
        if not match:
            warnings.append(f"`class {change.concept}(...)` not found; edit the module by hand.")
    for base in bases:
        if base not in cram.module_names:
            warnings.append(f"`{base}` is neither defined nor imported in {MODULE_FILE}; "
                            "add the import.")
    patch = _diff(MODULE_FILE, module, after)
    test, source = test_path(change.concept), test_source(change.concept)
    if (cram.root / test).is_file():
        warnings.append(f"`{test.as_posix()}` already exists; the patch leaves it alone.")
    else:
        patch += (f"--- /dev/null\n+++ b/{test.as_posix()}\n"
                  f"@@ -0,0 +1,{len(source.splitlines())} @@\n"
                  + "".join(f"+{line}\n" for line in source.splitlines()))
    return patch, warnings


def registry_patch(change: Change, registry: dict, cram: CramClasses) -> str:
    before = REGISTRY.read_text(encoding="utf-8")
    updated = json.loads(before)
    # Only this concept's own lines change, so that the pull requests of several concepts
    # merge without conflicts; the cram2 commit is recorded with the concept for that reason.
    entry = {"cram": change.cram_status}
    commit = cram.commit()
    if commit:
        entry["since"] = commit[:12]
    if change.kind == "withdraw" and "proposal" in updated["concepts"].get(change.concept, {}):
        entry["proposal"] = updated["concepts"][change.concept]["proposal"]
    updated["concepts"][change.concept] = entry
    if change.kind == "map-type":
        updated["concepts"] = dict(sorted(updated["concepts"].items()))
        updated["object_types"][change.object_type] = change.concept
        updated["object_types"] = dict(sorted(updated["object_types"].items()))
    after = json.dumps(updated, indent=1, ensure_ascii=False) + "\n"
    return _diff(REGISTRY.relative_to(ROOT), before, after)


def pull_request(change: Change, registry: dict, cram: CramClasses) -> tuple[str, str, str]:
    """``(description.md, steps.md, change.patch)`` for one change: the text reviewers read
    on GitHub, the instructions for whoever opens it, and the change itself."""
    ids = " ".join(o["id"] for o in change.objects)
    listed = "\n".join(f"- #{o['id']} {o['name']} (`{o['fingerprint']['type']}`)"
                       for o in change.objects) or "- none yet"
    branch = change.branch
    if change.repository == "cram2":
        entry = registry["concepts"][change.concept]
        patch, warnings = cram_patch(change, entry, cram)
        what = (f"Add the annotation class {change.concept}" if change.kind == "add-class"
                else f"Let {change.concept} annotate a body")
        why = (f"`{change.concept}` does not exist in semantic_digital_twin yet."
               if change.kind == "add-class" else
               f"`{change.concept}` exists but has no root body, so it cannot be attached to a "
               f"body; this adds {', '.join(entry['proposal']['add_bases'])} to its bases.")
        body = (f"{why} The private_meshes objects below are annotated with "
                f"`{registry['fallback']}` until it is available.\n\n{listed}\n\n"
                f"The test in `{test_path(change.concept).as_posix()}` checks that the class "
                "can annotate a body.")
        test = test_path(change.concept).as_posix()
        base = registry["cram"]["branch"]
        steps = (f"cd <cram2 checkout>\n"
                 f"git fetch <cram2 remote>     # the remote of {registry['cram']['repository']}\n"
                 f"git switch -c {branch} <cram2 remote>/{base}\n"
                 f"git apply --index <this folder>/change.patch\n"
                 f"python scripts/format_docstrings.py {MODULE_FILE.as_posix()} {test}\n"
                 f"git add -A && git diff --cached     # only the new lines and {Path(test).name}\n"
                 f"python -m pytest {test}\n"
                 f"git commit -m '{what}'\n"
                 f"git remote get-url origin   # must be your fork, never cram2\n"
                 f"git push -u origin {branch}\n"
                 f"gh pr create --repo {registry['cram']['repository']} --base {base} "
                 f"--title '{what}' --body-file <this folder>/description.md")
        after = (f"Keep the branch name `{branch}`: later runs find the pull request by it on "
                 f"GitHub and list it as waiting while it is open. Once merged, they report an "
                 f"`adopt` change for private_meshes, which switches these objects to the new class. "
                 f"If it is closed without merging, the concept counts as declined: the objects keep "
                 f"the fallback and the change is not proposed again.")
    else:
        patch, warnings = registry_patch(change, registry, cram), []
        if change.kind == "withdraw":
            warnings.append(f"cram2 no longer has a usable `{change.concept}` ({change.cram_status}); "
                            "these objects fall back until it is restored.")
        what = {"adopt": f"Annotate with {change.concept}, now in cram2",
                "withdraw": f"Fall back from {change.concept}, {change.cram_status} in cram2",
                "map-type": f"Annotate {change.object_type} objects with {change.concept}"}[change.kind]
        body = (f"cram2 reports `{change.concept}` as {change.cram_status}. This updates "
                f"`semantic_concepts.json` and the `semantics.json` of:\n\n{listed}")
        steps = (f"git switch -c {branch}\n"
                 f"git apply --index <this folder>/change.patch\n"
                 f"{GENERATE} {ids}\n"
                 f"python3 -m unittest discover -s tests\n"
                 f"git add -A objects/articulated && git commit -m '{what}'\n"
                 f"git push -u origin {branch}\n"
                 f"gh pr create --repo {PRIVATE_MESHES_REPOSITORY} --base main "
                 f"--title '{what}' --body-file <this folder>/description.md")
        after = "Nothing follows: the objects use the cram2 class directly."
    target = registry["cram"]["repository"] if change.repository == "cram2" else PRIVATE_MESHES_REPOSITORY
    notes = "".join(f"> **Check:** {w}\n\n" for w in warnings)
    instructions = (f"# {what}\n\n"
                    f"- **Pull request to:** `{target}`, branch `main`\n"
                    f"- **From branch:** `{branch}` (keep this name)\n"
                    f"- **Title:** `{what}`\n"
                    f"- **Description:** the contents of `description.md`\n\n"
                    f"{notes}## Steps (not run by sync_semantics.py)\n\n```sh\n{steps}\n```\n\n{after}\n")
    return f"{body}\n", instructions, patch


# --- command line -------------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=["status", "prepare"])
    parser.add_argument("--cram", type=Path, required=True, help="a cram2 checkout")
    parser.add_argument("--out", type=Path, default=ROOT / "semantic-sync",
                        help="where prepare writes one folder per pull request")
    parser.add_argument("--offline", action="store_true",
                        help="do not ask GitHub which pull requests are already open")
    args = parser.parse_args(argv)

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    objects = json.loads(COLLECTION.read_text(encoding="utf-8"))["objects"]
    cram = CramClasses.read(args.cram.expanduser().resolve())
    changes = compare(registry, cram, objects)
    commit = cram.commit()
    print(f"cram2 checkout {cram.root} at {commit[:9] if commit else 'unknown commit'}; "
          f"registry set up against {registry['cram']['checked'][:9]}")
    for concept, entry in registry["concepts"].items():
        mark = "" if entry["cram"] in (cram.status(concept), DECLINED) else "  ← differs"
        print(f"  {concept:22} registry {entry['cram']:9} cram2 {cram.status(concept):9}{mark}")

    unassigned = unassigned_types(registry, objects)
    if unassigned:
        print(f"{len(unassigned)} object type(s) without a concept (add them to object_types, "
              "or map them to null to keep the fallback on purpose):")
        for object_type, users in unassigned.items():
            hints = similar_concepts(object_type, registry, cram)
            ids = ", ".join(f"#{o['id']}" for o in users)
            print(f"  {object_type:32} {ids}" + (f"   similar: {', '.join(hints)}" if hints else ""))

    if args.offline:
        print("Offline: pull requests already opened are not looked up.")
    else:
        owners = {"cram2": fork_owner(cram.root), "private_meshes": fork_owner(ROOT)}
        problem = look_up_pull_requests(changes, registry, owners)
        if problem:
            print(f"Could not ask GitHub ({problem}); every change is prepared as if none were open.")
    pending = []
    for change in changes:
        found = change.pull_request
        if found is None:
            pending.append(change)
        elif found.state == OPEN:
            print(f"  waiting: [{change.repository}] {change.slug} is open: {found.url}")
        elif found.state == MERGED:
            update = (f"update {cram.root} to cram2's latest main" if change.repository == "cram2"
                      else "update this repository to the latest main")
            print(f"  merged:  [{change.repository}] {change.slug} ({found.url}); {update} to move on")
        else:
            print(f"  declined: [{change.repository}] {change.slug} was closed without merging "
                  f"({found.url}); {change.concept} keeps the fallback. Open a new pull request "
                  f"from {change.branch} to propose it again.")
    if not pending:
        print("In step: no new pull requests needed.")
    else:
        print(f"{len(pending)} pull request(s) to open:")
        for number, change in enumerate(pending, 1):
            print(f"  {number:02}. [{change.repository}] {change.slug} "
                  f"({len(change.objects)} object(s))")
    if args.command == "prepare":
        clear_output(args.out)
        for number, change in enumerate(pending, 1):
            folder = args.out / f"{number:02}-{change.repository}-{change.slug}"
            folder.mkdir(parents=True)
            description, steps, patch = pull_request(change, registry, cram)
            (folder / "description.md").write_text(description, encoding="utf-8")
            (folder / "steps.md").write_text(steps, encoding="utf-8")
            (folder / "change.patch").write_text(patch, encoding="utf-8")
        print(f"Prepared in {args.out} (earlier folders removed); nothing was committed or pushed.")
    return 0


def clear_output(out: Path) -> None:
    """Empty ``out`` of earlier prepare runs, so merged or replaced pull requests do not
    linger. Refuses when it holds anything prepare did not write."""
    if not out.exists():
        return
    foreign = [p.name for p in out.iterdir()
               if not (p.is_dir() and FOLDER.fullmatch(p.name)
                       and {f.name for f in p.iterdir()} <= PREPARED_FILES)]
    if foreign:
        raise SystemExit(f"{out} holds files prepare did not write ({', '.join(sorted(foreign))}); "
                         "choose another --out or move them away")
    for folder in out.iterdir():
        for file in folder.iterdir():
            file.unlink()
        folder.rmdir()


if __name__ == "__main__":
    sys.exit(main())
