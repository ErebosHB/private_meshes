# private_meshes

**Author and design direction:** Vanessa Hassouna (33067562+sunava@users.noreply.github.com), developed for AICOR Solutions.

Licensed under the [BSD 3-Clause License](LICENSE.txt), Copyright (c) 2026, Vanessa Hassouna. [NOTICE.md](NOTICE.md)
lists what the licence covers, the third-party exclusions, and the objects #001-#150
whose licence is still pending.

The independent object collection also has an automatically generated
[web catalogue](https://sunava.github.io/private_meshes/).
See [site/README.md](site/README.md) for the GitHub Pages setup, local
preview commands and instructions for adding objects.

This repository contains the assembled laboratory and its independent equipment:

- [`aicor_medical_lab`](aicor_medical_lab/README.md): the room, workbench, articulated
  drawer, instruments, rack and separate sample vessels. `scene.json` describes
  the assembled scene; `environment.urdf` describes the environment and
  articulated equipment. Meshes, materials and collision data are included.
- [`laboratory_devices`](laboratory_devices/README.md): five independently
  loadable instrument folders, listed below.
- [`centrifuge_manuals`](centrifuge_manuals/): the two operating-manual editions
  used by the laboratory knowledge demonstration.

The independent device models are:

| Device | URDF |
| --- | --- |
| Centrifuge with articulated lid and rotor | [`centrifuge/model.urdf`](laboratory_devices/centrifuge/model.urdf) |
| Dual dispenser | [`dual_dispenser/model.urdf`](laboratory_devices/dual_dispenser/model.urdf) |
| Laboratory scale | [`scale/model.urdf`](laboratory_devices/scale/model.urdf) |
| Tube rack | [`tube_rack/model.urdf`](laboratory_devices/tube_rack/model.urdf) |
| Sample refrigerator with articulated glass door | [`refrigerator/model.urdf`](laboratory_devices/refrigerator/model.urdf) |

Each device directory includes its URDF, visual meshes with embedded materials,
collision geometry, frame metadata, documentation and licence notices. To reuse a
device, copy the complete device directory, including its notices;
its mesh references remain relative. Units are
metres, with Z pointing up.

Load a model directly with CRAM's semantic digital twin:

```python
from semantic_digital_twin.adapters.urdf import URDFParser

world = URDFParser.from_file(
    "/path/to/private_meshes/laboratory_devices/centrifuge/model.urdf",
    prefix="centrifuge_one_",
).parse()
```

Use a distinct prefix for each instance. Loading these models does not require
the CRAMERA viewer. Instrument controllers and fluid simulation belong to the
laboratory application; loading a URDF supplies the geometry and articulation.

In the CRAMERA workspace this repository is checked out directly at
`cramera/src/cramera/resources`. Its `laboratory_devices` catalog can therefore
also be accessed through `cramera.laboratory_devices.LaboratoryDeviceResource`.
The `aicor_medical_lab`, `laboratory_devices` and `centrifuge_manuals` directories
are all versioned in this resource repository. The surrounding CRAMERA
repository currently also tracks these resource files for application packaging;
a commit in one repository does not automatically create a commit in the other.

The PR2 robot description and the CRAM/CRAMERA application source are separate
dependencies and are not included here.
