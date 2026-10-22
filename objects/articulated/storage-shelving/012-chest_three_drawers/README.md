# Chest of Three Drawers

Chest of three deep drawers on a recessed plinth with a pine top.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so each drawer box stays open from above.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `chest_three_drawers_lower_drawer_joint` | prismatic | 0.22 |
| `chest_three_drawers_middle_drawer_joint` | prismatic | 0.22 |
| `chest_three_drawers_upper_drawer_joint` | prismatic | 0.22 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `chest_three_drawers_lower_drawer_grip` | `chest_three_drawers_lower_drawer` | grasp |
| `chest_three_drawers_lower_drawer_volume` | `chest_three_drawers_lower_drawer` | container_volume |
| `chest_three_drawers_middle_drawer_grip` | `chest_three_drawers_middle_drawer` | grasp |
| `chest_three_drawers_middle_drawer_volume` | `chest_three_drawers_middle_drawer` | container_volume |
| `chest_three_drawers_upper_drawer_grip` | `chest_three_drawers_upper_drawer` | grasp |
| `chest_three_drawers_upper_drawer_volume` | `chest_three_drawers_upper_drawer` | container_volume |
| `chest_three_drawers_top_surface` | `chest_three_drawers_body` | place_surface |
| `chest_three_drawers_wall_anchor` | `chest_three_drawers_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model drawer runners, interlocks, load ratings, wall-fixing strength, assembly or tip-over behaviour.
