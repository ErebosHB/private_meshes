# Kitchen Dresser

Tall kitchen dresser with two drawers and two doors below a worktop, an open niche and a glazed two-door top cupboard.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per carcass panel, front, glass pane and drawer-box wall, so both cupboards, the drawers and the niche stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; glass 2,500; particleboard 650; pine 500 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `kitchen_dresser_left_drawer_joint` | prismatic | 0.276 |
| `kitchen_dresser_right_drawer_joint` | prismatic | 0.276 |
| `kitchen_dresser_left_door_joint` | revolute | 1.4 |
| `kitchen_dresser_right_door_joint` | revolute | 1.4 |
| `kitchen_dresser_top_left_glass_door_joint` | revolute | 1.4 |
| `kitchen_dresser_top_right_glass_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `kitchen_dresser_left_drawer_grip` | `kitchen_dresser_left_drawer` | grasp |
| `kitchen_dresser_left_drawer_volume` | `kitchen_dresser_left_drawer` | container_volume |
| `kitchen_dresser_right_drawer_grip` | `kitchen_dresser_right_drawer` | grasp |
| `kitchen_dresser_right_drawer_volume` | `kitchen_dresser_right_drawer` | container_volume |
| `kitchen_dresser_left_door_grip` | `kitchen_dresser_left_door` | grasp |
| `kitchen_dresser_right_door_grip` | `kitchen_dresser_right_door` | grasp |
| `kitchen_dresser_worktop_surface` | `kitchen_dresser_body` | place_surface |
| `kitchen_dresser_top_left_glass_door_grip` | `kitchen_dresser_top_left_glass_door` | grasp |
| `kitchen_dresser_top_right_glass_door_grip` | `kitchen_dresser_top_right_glass_door` | grasp |
| `kitchen_dresser_top_shelf_surface` | `kitchen_dresser_body` | place_surface |
| `kitchen_dresser_wall_anchor` | `kitchen_dresser_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model hinge dampers, drawer runners, load ratings, wall-fixing strength, assembly or tip-over behaviour.
