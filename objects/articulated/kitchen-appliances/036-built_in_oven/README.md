# Built-In Oven

Single wall oven with a drop-down glass door, a baking tray on telescopic rails and two control dials.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing, frame and cavity panel, and thin boxes for the shelf and tray, so the cavity stays open behind the door.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; aluminium 2,700; glass 2,500; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `built_in_oven_function_dial_joint` | revolute | 1.57 |
| `built_in_oven_temperature_dial_joint` | revolute | 1.57 |
| `built_in_oven_baking_tray_joint` | prismatic | 0.282 |
| `built_in_oven_door_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `built_in_oven_function_dial_contact` | `built_in_oven_function_dial` | control |
| `built_in_oven_temperature_dial_contact` | `built_in_oven_temperature_dial` | control |
| `built_in_oven_baking_tray_grip` | `built_in_oven_baking_tray` | grasp |
| `built_in_oven_baking_tray_surface` | `built_in_oven_baking_tray` | place_surface |
| `built_in_oven_door_grip` | `built_in_oven_door` | grasp |
| `built_in_oven_cavity_volume` | `built_in_oven_body` | container_volume |
| `built_in_oven_wire_shelf_surface` | `built_in_oven_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model heating, the fan, the door's hinge springs or cool-touch glazing, the cabinet fixing or load ratings.
