# Concrete Vibrator

Drive motor in a tubular carry frame with a flexible shaft, modelled as three bending segments, ending in a steel poker head.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one cylinder per frame tube, shaft segment and the poker, so the inside of the carry frame stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `concrete_vibrator_shaft_segment_1_joint` | revolute | 0.38 |
| `concrete_vibrator_shaft_segment_2_joint` | revolute | 0.38 |
| `concrete_vibrator_shaft_segment_3_joint` | revolute | 0.38 |
| `concrete_vibrator_power_switch_joint` | revolute | 0.35 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `concrete_vibrator_carry_grip` | `concrete_vibrator_body` | grasp |
| `concrete_vibrator_shaft_grip` | `concrete_vibrator_shaft_segment_1` | grasp |
| `concrete_vibrator_power_switch_contact` | `concrete_vibrator_power_switch` | control |
| `concrete_vibrator_poker_head` | `concrete_vibrator_shaft_segment_3` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model vibration frequency, the poker's eccentric, shaft flexibility beyond three segments, coupling torque or concrete.
