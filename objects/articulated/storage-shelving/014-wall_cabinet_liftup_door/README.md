# Wall Cabinet with Lift-up Door

Wall-hung cabinet with one lift-up door and an inner shelf.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at the back-bottom edge centre.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so the compartment stays open below the lifted door.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wall_cabinet_liftup_door_lift_door_joint` | revolute | 1.20 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wall_cabinet_liftup_door_lift_door_grip` | `wall_cabinet_liftup_door_lift_door` | grasp |
| `wall_cabinet_liftup_door_shelf_surface` | `wall_cabinet_liftup_door_body` | place_surface |
| `wall_cabinet_liftup_door_top_surface` | `wall_cabinet_liftup_door_body` | place_surface |
| `wall_cabinet_liftup_door_wall_anchor` | `wall_cabinet_liftup_door_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model lift-up stays or gas struts, load ratings, wall-fixing strength or assembly.
