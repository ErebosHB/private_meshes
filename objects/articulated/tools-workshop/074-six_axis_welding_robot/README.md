# Six-Axis Welding Robot

Floor-mounted articulated arm with six rotary axes and a swan-neck welding torch on its flange.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one cylinder or box per housing, joint drum and torch segment.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `six_axis_welding_robot_turret_joint` | revolute | 0.6 |
| `six_axis_welding_robot_lower_arm_joint` | revolute | 0.4 |
| `six_axis_welding_robot_upper_arm_joint` | revolute | 0.35 |
| `six_axis_welding_robot_forearm_joint` | revolute | 0.8 |
| `six_axis_welding_robot_wrist_joint` | revolute | 0.6 |
| `six_axis_welding_robot_flange_joint` | revolute | 1 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `six_axis_welding_robot_flange_mount` | `six_axis_welding_robot_flange` | tool_attachment |
| `six_axis_welding_robot_torch_tip` | `six_axis_welding_robot_flange` | tool_attachment |
| `six_axis_welding_robot_forearm_teach_grip` | `six_axis_welding_robot_forearm` | grasp |
| `six_axis_welding_robot_base_anchor` | `six_axis_welding_robot_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the servo drives, gearboxes, payload ratings, controller, wire feed through the arm or the welding process.
