# Folding Partition Screen

Three-panel acoustic screen whose outer panels fold on vertical hinges to stand free.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the middle panel's footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per frame rail, infill and foot, so the gaps between panels stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `folding_partition_screen_left_panel_joint` | revolute | 1 |
| `folding_partition_screen_right_panel_joint` | revolute | 1 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `folding_partition_screen_left_panel_grip` | `folding_partition_screen_left_panel` | grasp |
| `folding_partition_screen_right_panel_grip` | `folding_partition_screen_right_panel` | grasp |
| `folding_partition_screen_carry_grip` | `folding_partition_screen_body` | grasp |
| `folding_partition_screen_anti_tip_anchor` | `folding_partition_screen_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model sound absorption, hinge friction, panel linking clips, wind load or tip-over behaviour.
