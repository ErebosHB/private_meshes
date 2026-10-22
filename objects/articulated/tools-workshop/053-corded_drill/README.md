# Corded Drill

Two-speed pistol drill with a keyless chuck, swivelling side handle, gear selector, direction switch and trigger.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, grip and the chuck, so the gap between grip and side handle stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `corded_drill_chuck_joint` | continuous | 0.9 |
| `corded_drill_side_handle_joint` | revolute | 1.25 |
| `corded_drill_gear_selector_joint` | revolute | 3.14 |
| `corded_drill_direction_switch_joint` | prismatic | 0.008 |
| `corded_drill_trigger_joint` | prismatic | 0.008 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `corded_drill_pistol_grip` | `corded_drill_body` | grasp |
| `corded_drill_side_handle_grip` | `corded_drill_side_handle` | grasp |
| `corded_drill_trigger_contact` | `corded_drill_trigger` | control |
| `corded_drill_direction_switch_contact` | `corded_drill_direction_switch` | control |
| `corded_drill_gear_selector_contact` | `corded_drill_gear_selector` | control |
| `corded_drill_chuck_jaws` | `corded_drill_chuck` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model motor speed control, the gear stages, the slip clutch, chuck clamping force or the impact function.
