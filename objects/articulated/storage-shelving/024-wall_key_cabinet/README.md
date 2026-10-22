# Wall Key Cabinet

Wall-hung steel cabinet with one hinged door, a turn knob and four rows of key hooks.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at the back-bottom edge centre.
Use a unique URDF parser prefix for each instance.
Collision uses one box per sheet-steel wall and hook rail, so the key compartment stays open behind the door.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wall_key_cabinet_door_joint` | revolute | 1.4 |
| `wall_key_cabinet_lock_knob_joint` | revolute | 1.57 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wall_key_cabinet_hook_row_1` | `wall_key_cabinet_body` | tool_attachment |
| `wall_key_cabinet_hook_row_2` | `wall_key_cabinet_body` | tool_attachment |
| `wall_key_cabinet_hook_row_3` | `wall_key_cabinet_body` | tool_attachment |
| `wall_key_cabinet_hook_row_4` | `wall_key_cabinet_body` | tool_attachment |
| `wall_key_cabinet_door_grip` | `wall_key_cabinet_lock_knob` | grasp |
| `wall_key_cabinet_lock_knob_contact` | `wall_key_cabinet_lock_knob` | control |
| `wall_key_cabinet_wall_anchor` | `wall_key_cabinet_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the lock mechanism, key tags, wall-fixing strength or the door's hinge stops.
