#!/usr/bin/env python3
"""Build the object catalogue using Python's standard library only."""
from __future__ import annotations

import json
import re
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath
from urllib.parse import quote
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def local_path(base: Path, value: str) -> Path:
    """Accept only ordinary paths contained in base, never symlinks."""
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError(f"Unsafe relative path: {value!r}")
    candidate = base.joinpath(*path.parts)
    if not candidate.resolve().is_relative_to(base.resolve()):
        raise ValueError(f"Path escapes source directory: {value}")
    if any(part.is_symlink() for part in (candidate, *candidate.parents)):
        raise ValueError(f"Symlinks are not supported: {value}")
    return candidate


def read_catalogue(root: Path) -> dict:
    source = root / "objects" / "articulated"
    data = json.loads((source / "collection.json").read_text(encoding="utf-8"))
    categories = {c["key"]: c for c in data["categories"]}
    if len(categories) != len(data["categories"]):
        raise ValueError("Duplicate category keys")
    for key in categories:
        if not re.fullmatch(r"[a-z0-9-]+", key):
            raise ValueError(f"Invalid category key: {key}")
    ids, folders = set(), set()
    for obj in data["objects"]:
        ident = obj["id"]
        if not isinstance(ident, str) or not re.fullmatch(r"[0-9]+", ident):
            raise ValueError(f"Invalid object ID: {ident}")
        if ident in ids or obj["folder"] in folders:
            raise ValueError(f"Duplicate object ID or folder: {ident}")
        ids.add(ident)
        folders.add(obj["folder"])
        if obj["category"] not in categories:
            raise ValueError(f"Unknown category for {ident}")
        folder = local_path(source, obj["folder"])
        if folder.relative_to(source).parts[0] != obj["category"]:
            raise ValueError(f"Category/folder mismatch for {ident}")
        for required in ("model.blend", "model.urdf", "README.md", "NOTICE.md",
                         "renders/rest.webp", "renders/open.webp"):
            if not local_path(folder, required).is_file():
                raise ValueError(f"Missing {obj['folder']}/{required}")
        for file in folder.rglob("*"):
            local_path(folder, file.relative_to(folder).as_posix())
        for mesh in ET.parse(folder / "model.urdf").iter("mesh"):
            filename = mesh.attrib.get("filename", "")
            if not local_path(folder, filename).is_file():
                raise ValueError(f"Missing mesh for {ident}: {filename}")
        obj["url"] = "models/" + quote(obj["folder"], safe="/")
        obj["download"] = f"downloads/{ident}-{folder.name.split('-', 1)[-1]}.zip"
    actual = {p.parent.relative_to(source).as_posix() for p in source.rglob("model.urdf")}
    if actual != folders:
        raise ValueError(f"Catalogue/folder mismatch: {sorted(actual ^ folders)}")
    for category in data["categories"]:
        category["count"] = sum(o["category"] == category["key"] for o in data["objects"])
    data["stats"] = {
        "objects": len(data["objects"]), "categories": len(categories),
        "joints": sum(len(o.get("joints", [])) for o in data["objects"]),
        "frames": sum(len(o.get("frames", [])) for o in data["objects"]),
    }
    return data


def add_to_zip(archive: ZipFile, file: Path, name: str) -> None:
    info = ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, file.read_bytes())


def build(root: Path) -> dict:
    # Validate before touching the previous build. Output is always root/dist.
    root = root.resolve()
    data = read_catalogue(root)
    output = root / "dist"
    if output.is_symlink():
        raise ValueError("dist must not be a symlink")
    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    for name in ("index.html", "styles.css", "app.js"):
        shutil.copyfile(root / "site" / name, output / name)
    (output / ".nojekyll").touch()
    (output / "downloads").mkdir()
    (output / "catalogue.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    shutil.copyfile(root / "NOTICE.md", output / "NOTICE.md")
    shutil.copyfile(root / "LICENSE.txt", output / "LICENSE.txt")
    for obj in data["objects"]:
        folder = root / "objects" / "articulated" / obj["folder"]
        target = output / "models" / obj["folder"]
        (target / "renders").mkdir(parents=True)
        for name in ("renders/rest.webp", "renders/open.webp", "README.md", "NOTICE.md"):
            shutil.copyfile(folder / name, target / name)
        if (folder / "semantics.json").is_file():
            shutil.copyfile(folder / "semantics.json", target / "semantics.json")
        with ZipFile(output / obj["download"], "w") as archive:
            for file in sorted(folder.rglob("*")):
                if file.is_file():
                    add_to_zip(archive, file, f"{folder.name}/{file.relative_to(folder).as_posix()}")
            # Preserve the repository's licence scope as well as the object notices.
            add_to_zip(archive, root / "NOTICE.md", f"{folder.name}/_repository/NOTICE.md")
            add_to_zip(archive, root / "LICENSE.txt", f"{folder.name}/_repository/LICENSE.txt")
    return data["stats"]


if __name__ == "__main__":
    stats = build(Path(__file__).resolve().parents[1])
    print(f"Built {stats['objects']} objects in {stats['categories']} categories into dist/")
