# private_meshes

Reusable AICOR laboratory equipment for CRAM. The four independent models live
in [`laboratory_devices`](laboratory_devices/README.md):

| Device | URDF |
| --- | --- |
| Centrifuge with articulated lid and rotor | [`centrifuge/model.urdf`](laboratory_devices/centrifuge/model.urdf) |
| Dual dispenser | [`dual_dispenser/model.urdf`](laboratory_devices/dual_dispenser/model.urdf) |
| Laboratory scale | [`scale/model.urdf`](laboratory_devices/scale/model.urdf) |
| Tube rack | [`tube_rack/model.urdf`](laboratory_devices/tube_rack/model.urdf) |

Each device directory includes its URDF, visual meshes with embedded materials,
collision geometry, frame metadata and documentation. Copy the complete device
directory to another project; its mesh references remain relative. Units are
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
The neighbouring `precision_lab` and `centrifuge_manuals` directories are managed
by the surrounding CRAMERA repository and are not part of this device catalog.
