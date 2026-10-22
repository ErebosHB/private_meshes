# Wardrobe Frame with Hinged Doors

Full-height wardrobe frame with two hinged doors, a hat shelf and a hanging rail.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so the hanging space stays open behind the doors.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wardrobe_frame_hinged_doors_left_door_joint` | revolute | 1.40 |
| `wardrobe_frame_hinged_doors_right_door_joint` | revolute | 1.40 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wardrobe_frame_hinged_doors_left_door_grip` | `wardrobe_frame_hinged_doors_left_door` | grasp |
| `wardrobe_frame_hinged_doors_right_door_grip` | `wardrobe_frame_hinged_doors_right_door` | grasp |
| `wardrobe_frame_hinged_doors_hat_shelf_surface` | `wardrobe_frame_hinged_doors_body` | place_surface |
| `wardrobe_frame_hinged_doors_wall_anchor` | `wardrobe_frame_hinged_doors_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model hinge dampers, clothes-rail load, wall-fixing strength, assembly or tip-over behaviour.
