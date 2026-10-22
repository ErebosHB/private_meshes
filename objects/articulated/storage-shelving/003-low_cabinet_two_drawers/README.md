# Low Cabinet, Two Drawers

Low cabinet on pine block legs with two side-by-side drawers.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so both drawer boxes stay open from above.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `low_cabinet_two_drawers_left_drawer_joint` | prismatic | 0.18 |
| `low_cabinet_two_drawers_right_drawer_joint` | prismatic | 0.18 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `low_cabinet_two_drawers_left_drawer_grip` | `low_cabinet_two_drawers_left_drawer` | grasp |
| `low_cabinet_two_drawers_left_drawer_volume` | `low_cabinet_two_drawers_left_drawer` | container_volume |
| `low_cabinet_two_drawers_right_drawer_grip` | `low_cabinet_two_drawers_right_drawer` | grasp |
| `low_cabinet_two_drawers_right_drawer_volume` | `low_cabinet_two_drawers_right_drawer` | container_volume |
| `low_cabinet_two_drawers_top_surface` | `low_cabinet_two_drawers_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model drawer runners, load ratings, assembly or tip-over behaviour.
