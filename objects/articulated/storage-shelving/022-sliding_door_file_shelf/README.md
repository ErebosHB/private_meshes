# File Shelf with Sliding Doors

Three-height folder shelf closed by two sliding doors running on separate tracks.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, track and door, so all three compartments stay open behind the doors.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `sliding_door_file_shelf_front_door_joint` | prismatic | 0.57 |
| `sliding_door_file_shelf_rear_door_joint` | prismatic | 0 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `sliding_door_file_shelf_front_door_grip` | `sliding_door_file_shelf_front_door` | grasp |
| `sliding_door_file_shelf_rear_door_grip` | `sliding_door_file_shelf_rear_door` | grasp |
| `sliding_door_file_shelf_bottom_surface` | `sliding_door_file_shelf_body` | place_surface |
| `sliding_door_file_shelf_shelf_1_surface` | `sliding_door_file_shelf_body` | place_surface |
| `sliding_door_file_shelf_shelf_2_surface` | `sliding_door_file_shelf_body` | place_surface |
| `sliding_door_file_shelf_top_surface` | `sliding_door_file_shelf_body` | place_surface |
| `sliding_door_file_shelf_wall_anchor` | `sliding_door_file_shelf_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the track rollers, door locks, shelf load ratings, wall-fixing strength or tip-over behaviour.
