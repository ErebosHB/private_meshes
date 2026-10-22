# Cantilever Rack with Flip-up Stops

Single-sided cantilever rack for long stock: two columns with four arm levels, each arm ending in a flip-up stop.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per column flange, foot, brace and arm, so the space between the arms stays open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; hollow steel profiles as an equivalent 1,900; ABS/HDPE 1,050 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `cantilever_rack_left_stop_1_joint` | revolute | 1.5 |
| `cantilever_rack_left_stop_2_joint` | revolute | 1.5 |
| `cantilever_rack_left_stop_3_joint` | revolute | 1.5 |
| `cantilever_rack_left_stop_4_joint` | revolute | 1.5 |
| `cantilever_rack_right_stop_1_joint` | revolute | 1.5 |
| `cantilever_rack_right_stop_2_joint` | revolute | 1.5 |
| `cantilever_rack_right_stop_3_joint` | revolute | 1.5 |
| `cantilever_rack_right_stop_4_joint` | revolute | 1.5 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `cantilever_rack_level_1_arm_surface` | `cantilever_rack_body` | place_surface |
| `cantilever_rack_level_2_arm_surface` | `cantilever_rack_body` | place_surface |
| `cantilever_rack_level_3_arm_surface` | `cantilever_rack_body` | place_surface |
| `cantilever_rack_level_4_arm_surface` | `cantilever_rack_body` | place_surface |
| `cantilever_rack_wall_anchor` | `cantilever_rack_body` | wall_mount |
| `cantilever_rack_left_stop_1_grip` | `cantilever_rack_left_stop_1` | grasp |
| `cantilever_rack_left_stop_2_grip` | `cantilever_rack_left_stop_2` | grasp |
| `cantilever_rack_left_stop_3_grip` | `cantilever_rack_left_stop_3` | grasp |
| `cantilever_rack_left_stop_4_grip` | `cantilever_rack_left_stop_4` | grasp |
| `cantilever_rack_right_stop_1_grip` | `cantilever_rack_right_stop_1` | grasp |
| `cantilever_rack_right_stop_2_grip` | `cantilever_rack_right_stop_2` | grasp |
| `cantilever_rack_right_stop_3_grip` | `cantilever_rack_right_stop_3` | grasp |
| `cantilever_rack_right_stop_4_grip` | `cantilever_rack_right_stop_4` | grasp |

The URDF supplies geometry, articulation and frames. It does not model arm deflection, arm height adjustment, load ratings per arm, anchor bolts or tip-over behaviour.
