# Sideboard, Drawers and Doors

Low credenza on steel legs with two drawers and a two-door cupboard with a shelf.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel and drawer wall, so the drawers and cupboard stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `sideboard_drawer_1_joint` | prismatic | 0.228 |
| `sideboard_drawer_2_joint` | prismatic | 0.228 |
| `sideboard_left_door_joint` | revolute | 1.4 |
| `sideboard_right_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `sideboard_drawer_1_grip` | `sideboard_drawer_1` | grasp |
| `sideboard_drawer_1_volume` | `sideboard_drawer_1` | container_volume |
| `sideboard_drawer_2_grip` | `sideboard_drawer_2` | grasp |
| `sideboard_drawer_2_volume` | `sideboard_drawer_2` | container_volume |
| `sideboard_left_door_grip` | `sideboard_left_door` | grasp |
| `sideboard_right_door_grip` | `sideboard_right_door` | grasp |
| `sideboard_cupboard_bottom_surface` | `sideboard_body` | place_surface |
| `sideboard_cupboard_shelf_surface` | `sideboard_body` | place_surface |
| `sideboard_top_surface` | `sideboard_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model drawer runners, soft-close hinges, locks or shelf load ratings.
