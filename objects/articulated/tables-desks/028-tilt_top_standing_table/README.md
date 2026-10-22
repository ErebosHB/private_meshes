# Tilt-Top Standing Table

Round standing table on a cross base whose top tilts upright for storage.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base bar, column, bracket and the round top.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `tilt_top_standing_table_table_top_joint` | revolute | 1.2 |
| `tilt_top_standing_table_tilt_release_joint` | revolute | 0.55 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `tilt_top_standing_table_tilt_release_tip` | `tilt_top_standing_table_tilt_release` | control |
| `tilt_top_standing_table_table_top_surface` | `tilt_top_standing_table_table_top` | place_surface |
| `tilt_top_standing_table_table_top_edge_grip` | `tilt_top_standing_table_table_top` | grasp |
| `tilt_top_standing_table_anti_tip_anchor` | `tilt_top_standing_table_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the tilt latch spring, levelling glides, load ratings or tip-over behaviour.
