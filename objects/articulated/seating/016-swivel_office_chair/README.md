# Swivel Office Chair

Task chair on a five-star base with gas lift, swivel seat, reclining back and height lever.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base leg, column, cushion, armrest and backrest.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `swivel_office_chair_castor_1_joint` | continuous | 0 |
| `swivel_office_chair_castor_2_joint` | continuous | 0 |
| `swivel_office_chair_castor_3_joint` | continuous | 0 |
| `swivel_office_chair_castor_4_joint` | continuous | 0 |
| `swivel_office_chair_castor_5_joint` | continuous | 0 |
| `swivel_office_chair_lift_joint` | prismatic | 0.12 |
| `swivel_office_chair_seat_joint` | continuous | 0.6 |
| `swivel_office_chair_height_lever_joint` | revolute | 0.28 |
| `swivel_office_chair_backrest_joint` | revolute | 0.3 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `swivel_office_chair_left_armrest_grip` | `swivel_office_chair_seat` | grasp |
| `swivel_office_chair_right_armrest_grip` | `swivel_office_chair_seat` | grasp |
| `swivel_office_chair_height_lever_tip` | `swivel_office_chair_height_lever` | control |
| `swivel_office_chair_seat_surface` | `swivel_office_chair_seat` | place_surface |
| `swivel_office_chair_backrest_top_grip` | `swivel_office_chair_backrest` | grasp |
| `swivel_office_chair_tether_anchor` | `swivel_office_chair_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the gas spring force, the recline spring tension, castor swivel, load ratings or tip-over behaviour.
