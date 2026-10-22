#!/usr/bin/env python3
"""Opt-in, local compatibility links for consumers using the former layout."""
from pathlib import Path

LEGACY_PATHS = {
    "objects_individually": "objects/articulated",
    "laboratory_devices": "objects/laboratory",
    "aicor_medical_lab": "environments/aicor_medical_lab",
    "centrifuge_manuals": "objects/laboratory/centrifuge/manuals",
}


def create_links(root: Path) -> None:
    root = root.resolve()
    # Check every destination before creating anything. Never replace user data.
    for old, new in LEGACY_PATHS.items():
        source, target = root / old, root / new
        if not target.is_dir():
            raise ValueError(f"Missing canonical directory: {new}")
        if source.is_symlink():
            if source.resolve() != target.resolve():
                raise FileExistsError(f"Refusing to replace existing symlink: {old}")
        elif source.exists():
            raise FileExistsError(f"Refusing to replace existing file or directory: {old}")
    for old, new in LEGACY_PATHS.items():
        source = root / old
        if not source.is_symlink():
            source.symlink_to(new, target_is_directory=True)


if __name__ == "__main__":
    try:
        create_links(Path(__file__).resolve().parents[1])
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error
    for old, new in LEGACY_PATHS.items():
        print(f"{old}/ -> {new}/")
