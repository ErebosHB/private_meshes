# Electric Kettle

Cordless kettle on a power base with a flip-up lid, a side handle and a rocker power switch.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses a disc for the base and foot, twelve wall segments for the jug and boxes for the handle and spout, so the jug interior stays open below the lid.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; glass 2,500; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `kettle_lid_joint` | revolute | 1.2 |
| `kettle_power_switch_joint` | revolute | 0.3 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `kettle_lid_grip` | `kettle_lid` | grasp |
| `kettle_power_switch_contact` | `kettle_power_switch` | control |
| `kettle_handle_grip` | `kettle_body` | grasp |
| `kettle_water_volume` | `kettle_body` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model heating, boiling, the thermostat cut-out, the lid latch, the jug lifting off its base or pouring.
