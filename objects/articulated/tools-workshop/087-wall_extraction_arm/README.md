# Wall-Mounted Fume Extraction Arm

Articulated extraction arm on a wall bracket: swivel head, inner and outer duct arms and a tilting capture hood, shown parked and reaching out.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at the back-bottom edge centre of the wall bracket.
Use a unique URDF parser prefix for each instance.
Collision uses boxes around each duct and the hood wall, so the duct bore and hood mouth stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wall_extraction_arm_swivel_head_joint` | revolute | 0.6 |
| `wall_extraction_arm_inner_arm_joint` | revolute | 1.1 |
| `wall_extraction_arm_outer_arm_joint` | revolute | 2.03 |
| `wall_extraction_arm_hood_joint` | revolute | 0.7 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wall_extraction_arm_hood_handle_grip` | `wall_extraction_arm_hood` | grasp |
| `wall_extraction_arm_wall_anchor` | `wall_extraction_arm_body` | wall_mount |
| `wall_extraction_arm_duct_outlet` | `wall_extraction_arm_body` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model airflow, the friction joints, gas-strut force, the flexible hose or the fan.
