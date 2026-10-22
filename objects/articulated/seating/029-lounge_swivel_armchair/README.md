# Lounge Swivel Armchair

Upholstered reception armchair on a disc base that swivels a full turn.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per cushion, arm and backrest block, plus cylinders for the base and column.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `lounge_swivel_armchair_seat_shell_joint` | continuous | 0.8 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `lounge_swivel_armchair_left_arm_grip` | `lounge_swivel_armchair_seat_shell` | grasp |
| `lounge_swivel_armchair_right_arm_grip` | `lounge_swivel_armchair_seat_shell` | grasp |
| `lounge_swivel_armchair_seat_surface` | `lounge_swivel_armchair_seat_shell` | place_surface |
| `lounge_swivel_armchair_backrest_top_grip` | `lounge_swivel_armchair_seat_shell` | grasp |

The URDF supplies geometry, articulation and frames. It does not model foam compliance, the swivel return mechanism, fabric wear or load ratings.
