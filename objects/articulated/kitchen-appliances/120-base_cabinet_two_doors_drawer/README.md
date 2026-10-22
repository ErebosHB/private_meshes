# Base Cabinet, Two Doors and Drawer

1 m kitchen base cabinet with worktop, a full-width drawer over two hinged doors and an inner shelf.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per carcass panel, front and drawer-box wall, so the cupboard and every drawer stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; particleboard 650; pine 500 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `base_cabinet_two_doors_drawer_drawer_joint` | prismatic | 0.258 |
| `base_cabinet_two_doors_drawer_left_door_joint` | revolute | 1.4 |
| `base_cabinet_two_doors_drawer_right_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `base_cabinet_two_doors_drawer_drawer_grip` | `base_cabinet_two_doors_drawer_drawer` | grasp |
| `base_cabinet_two_doors_drawer_drawer_volume` | `base_cabinet_two_doors_drawer_drawer` | container_volume |
| `base_cabinet_two_doors_drawer_left_door_grip` | `base_cabinet_two_doors_drawer_left_door` | grasp |
| `base_cabinet_two_doors_drawer_right_door_grip` | `base_cabinet_two_doors_drawer_right_door` | grasp |
| `base_cabinet_two_doors_drawer_shelf_surface` | `base_cabinet_two_doors_drawer_body` | place_surface |
| `base_cabinet_two_doors_drawer_worktop_surface` | `base_cabinet_two_doors_drawer_body` | place_surface |
| `base_cabinet_two_doors_drawer_wall_anchor` | `base_cabinet_two_doors_drawer_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model hinge dampers, drawer runners, load ratings, wall-fixing strength, assembly or tip-over behaviour.
