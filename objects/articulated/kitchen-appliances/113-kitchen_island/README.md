# Kitchen Island

Free-standing island with double doors and a three-drawer stack on the working side and two open shelves on the back.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per carcass panel, front, shelf and drawer-box wall, so the cupboard, the drawers and the back shelves stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; particleboard 650; pine 500 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `kitchen_island_b1_left_door_joint` | revolute | 1.4 |
| `kitchen_island_b1_right_door_joint` | revolute | 1.4 |
| `kitchen_island_b2_top_drawer_joint` | prismatic | 0.276 |
| `kitchen_island_b2_middle_drawer_joint` | prismatic | 0.276 |
| `kitchen_island_b2_bottom_drawer_joint` | prismatic | 0.276 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `kitchen_island_b1_left_door_grip` | `kitchen_island_b1_left_door` | grasp |
| `kitchen_island_b1_right_door_grip` | `kitchen_island_b1_right_door` | grasp |
| `kitchen_island_b2_top_drawer_grip` | `kitchen_island_b2_top_drawer` | grasp |
| `kitchen_island_b2_top_drawer_volume` | `kitchen_island_b2_top_drawer` | container_volume |
| `kitchen_island_b2_middle_drawer_grip` | `kitchen_island_b2_middle_drawer` | grasp |
| `kitchen_island_b2_middle_drawer_volume` | `kitchen_island_b2_middle_drawer` | container_volume |
| `kitchen_island_b2_bottom_drawer_grip` | `kitchen_island_b2_bottom_drawer` | grasp |
| `kitchen_island_b2_bottom_drawer_volume` | `kitchen_island_b2_bottom_drawer` | container_volume |
| `kitchen_island_back_lower_shelf_surface` | `kitchen_island_body` | place_surface |
| `kitchen_island_back_upper_shelf_surface` | `kitchen_island_body` | place_surface |
| `kitchen_island_worktop_surface` | `kitchen_island_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model hinge dampers, drawer runners, load ratings, wall-fixing strength, assembly or tip-over behaviour.
