# Swivel Bar Stool

Counter-height stool with gas lift, swivel seat, low backrest and a foot ring.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one cylinder per base, tube and seat plus one box per foot-ring segment, so the ring stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `swivel_bar_stool_lift_joint` | prismatic | 0.18 |
| `swivel_bar_stool_seat_joint` | continuous | 0.8 |
| `swivel_bar_stool_height_lever_joint` | revolute | 0.28 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `swivel_bar_stool_height_lever_tip` | `swivel_bar_stool_height_lever` | control |
| `swivel_bar_stool_seat_surface` | `swivel_bar_stool_seat` | place_surface |
| `swivel_bar_stool_backrest_grip` | `swivel_bar_stool_seat` | grasp |
| `swivel_bar_stool_tether_anchor` | `swivel_bar_stool_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the gas spring force, the swivel bearing friction, load ratings or tip-over behaviour.
