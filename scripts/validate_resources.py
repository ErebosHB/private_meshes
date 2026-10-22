#!/usr/bin/env python3
"""Check local asset references in both canonical resource groups."""
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from build_site import local_path

JSON_FILE_KEYS = {"mesh", "urdf", "trajectory", "asset", "doorAsset", "licenseFile", "noticeFile"}


def json_references(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in JSON_FILE_KEYS and isinstance(child, str):
                yield child
            else:
                yield from json_references(child)
    elif isinstance(value, list):
        for child in value:
            yield from json_references(child)


def validate(root: Path) -> dict:
    root = root.resolve()
    stats = {"urdfs": 0, "json_files": 0, "references": 0}
    for group in ("objects", "environments"):
        directory = local_path(root, group)
        if not directory.is_dir():
            raise ValueError(f"Missing asset directory: {group}")
        for file in sorted(directory.rglob("*")):
            local_path(root, file.relative_to(root).as_posix())
            if file.suffix == ".urdf":
                robot = ET.parse(file).getroot()
                if robot.tag != "robot":
                    raise ValueError(f"Invalid URDF root: {file.relative_to(root)}")
                refs = [element.attrib["filename"] for element in robot.iter()
                        if element.tag in {"mesh", "texture"} and "filename" in element.attrib]
                stats["urdfs"] += 1
            elif file.suffix == ".json":
                refs = list(json_references(json.loads(file.read_text(encoding="utf-8"))))
                stats["json_files"] += 1
            else:
                continue
            for reference in refs:
                if not local_path(file.parent, reference).is_file():
                    raise ValueError(f"Missing resource in {file.relative_to(root)}: {reference}")
                stats["references"] += 1
    return stats


if __name__ == "__main__":
    result = validate(Path(__file__).resolve().parents[1])
    print(f"Validated {result['urdfs']} URDFs, {result['json_files']} JSON files "
          f"and {result['references']} local resource references")
