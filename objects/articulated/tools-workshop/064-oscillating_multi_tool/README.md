# Oscillating Multi-Tool

Stick-body multi-cutter lying flat, with a flip-up quick-release lever, an oscillating blade holder, slide switch and speed wheel.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, head part and the blade.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `oscillating_multi_tool_blade_holder_joint` | revolute | 0.035 |
| `oscillating_multi_tool_release_lever_joint` | revolute | 1.3 |
| `oscillating_multi_tool_slide_switch_joint` | prismatic | 0.01 |
| `oscillating_multi_tool_speed_wheel_joint` | revolute | 2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `oscillating_multi_tool_body_grip` | `oscillating_multi_tool_body` | grasp |
| `oscillating_multi_tool_release_lever_tip` | `oscillating_multi_tool_release_lever` | control |
| `oscillating_multi_tool_slide_switch_contact` | `oscillating_multi_tool_slide_switch` | control |
| `oscillating_multi_tool_speed_wheel_contact` | `oscillating_multi_tool_speed_wheel` | control |
| `oscillating_multi_tool_blade_edge` | `oscillating_multi_tool_blade_holder` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the oscillation amplitude and frequency, accessory clamping force, vibration damping or blade wear.
