# Media Bench with Drop-down Flaps

Low media bench with three compartments behind drop-down flaps.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so all three compartments stay open behind the flaps.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `media_bench_dropdown_flaps_left_flap_joint` | revolute | 1.20 |
| `media_bench_dropdown_flaps_middle_flap_joint` | revolute | 1.20 |
| `media_bench_dropdown_flaps_right_flap_joint` | revolute | 1.20 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `media_bench_dropdown_flaps_left_flap_grip` | `media_bench_dropdown_flaps_left_flap` | grasp |
| `media_bench_dropdown_flaps_middle_flap_grip` | `media_bench_dropdown_flaps_middle_flap` | grasp |
| `media_bench_dropdown_flaps_right_flap_grip` | `media_bench_dropdown_flaps_right_flap` | grasp |
| `media_bench_dropdown_flaps_middle_shelf_surface` | `media_bench_dropdown_flaps_body` | place_surface |
| `media_bench_dropdown_flaps_top_surface` | `media_bench_dropdown_flaps_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model flap stays or dampers, cable routing, load ratings, assembly or tip-over behaviour.
