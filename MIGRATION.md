# Asset directory migration

The two asset groups are now `objects/` and `environments/`.

| Previous path | Canonical path |
| --- | --- |
| `objects_individually/` | `objects/articulated/` |
| `laboratory_devices/` | `objects/laboratory/` |
| `aicor_medical_lab/` | `environments/aicor_medical_lab/` |
| `centrifuge_manuals/` | `objects/laboratory/centrifuge/manuals/` |

Object IDs, mesh contents, URDF link/joint names, relative asset references and
scene placements have not changed. The website's public model/download URLs and
object deep links also remain stable. Catalogue authoring now uses
`objects/articulated/collection.json`.

## Applications using the old paths

Prefer updating the resource roots in the consuming application. For example,
CRAMERA's device catalogue should resolve `resources/objects/laboratory/`, and its
scene loader should resolve `resources/environments/aicor_medical_lab/`.
Its Python module name `cramera.laboratory_devices` does not need to change just
because the asset directory moved. Update package-data rules and exporter output
paths in that separate application as well.

For an existing checkout that still needs the old paths, run from this repository:

```sh
python3 scripts/link_legacy_paths.py
```

The helper creates four local relative directory symlinks. It makes no duplicate
asset copies, is safe to rerun, and refuses to overwrite any existing file or
directory. The aliases are ignored by Git and are not included in the website.
Symlink creation may require developer mode or additional permissions on Windows.

These aliases support filesystem consumers. They do not restore old GitHub blob
URLs or automatically change an application's installed package. New code and
documentation should use the canonical paths above.
