# Sliding-Door Wardrobe

Wide wardrobe with two bypass sliding doors over a hanging bay and a shelved bay.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so both bays stay open behind the doors.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `sliding_door_wardrobe_left_door_joint` | prismatic | 0.38 |
| `sliding_door_wardrobe_right_door_joint` | prismatic | 0.38 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `sliding_door_wardrobe_left_door_grip` | `sliding_door_wardrobe_left_door` | grasp |
| `sliding_door_wardrobe_right_door_grip` | `sliding_door_wardrobe_right_door` | grasp |
| `sliding_door_wardrobe_left_hat_shelf_surface` | `sliding_door_wardrobe_body` | place_surface |
| `sliding_door_wardrobe_right_lower_shelf_surface` | `sliding_door_wardrobe_body` | place_surface |
| `sliding_door_wardrobe_right_upper_shelf_surface` | `sliding_door_wardrobe_body` | place_surface |
| `sliding_door_wardrobe_wall_anchor` | `sliding_door_wardrobe_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model door rollers, soft-close, clothes-rail load, wall-fixing strength, assembly or tip-over behaviour.
