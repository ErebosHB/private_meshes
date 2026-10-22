# Tall Office Cabinet, Two Doors

Full-height cabinet with two hinged doors and four shelves for folders.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so all five compartments stay open behind the doors.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `tall_office_cabinet_left_door_joint` | revolute | 1.4 |
| `tall_office_cabinet_right_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `tall_office_cabinet_left_door_grip` | `tall_office_cabinet_left_door` | grasp |
| `tall_office_cabinet_right_door_grip` | `tall_office_cabinet_right_door` | grasp |
| `tall_office_cabinet_bottom_surface` | `tall_office_cabinet_body` | place_surface |
| `tall_office_cabinet_shelf_1_surface` | `tall_office_cabinet_body` | place_surface |
| `tall_office_cabinet_shelf_2_surface` | `tall_office_cabinet_body` | place_surface |
| `tall_office_cabinet_shelf_3_surface` | `tall_office_cabinet_body` | place_surface |
| `tall_office_cabinet_shelf_4_surface` | `tall_office_cabinet_body` | place_surface |
| `tall_office_cabinet_top_surface` | `tall_office_cabinet_body` | place_surface |
| `tall_office_cabinet_wall_anchor` | `tall_office_cabinet_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model hinge dampers, door locks, shelf load ratings, wall-fixing strength, assembly or tip-over behaviour.
