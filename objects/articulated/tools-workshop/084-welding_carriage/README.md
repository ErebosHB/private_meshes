# Track Welding Carriage

Motorised four-wheel welding carriage with a cross slide and a vertical slide holding the torch, a clutch lever and a speed knob.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per chassis block, slide, wheel and handle segment.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `welding_carriage_wheel_1_joint` | continuous | 0 |
| `welding_carriage_wheel_2_joint` | continuous | 0 |
| `welding_carriage_wheel_3_joint` | continuous | 0 |
| `welding_carriage_wheel_4_joint` | continuous | 0 |
| `welding_carriage_cross_slide_joint` | prismatic | 0.07 |
| `welding_carriage_vertical_slide_joint` | prismatic | 0.03 |
| `welding_carriage_clutch_lever_joint` | revolute | 1 |
| `welding_carriage_speed_knob_joint` | revolute | 2.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `welding_carriage_carry_handle_grip` | `welding_carriage_body` | grasp |
| `welding_carriage_torch_tip` | `welding_carriage_vertical_slide` | tool_attachment |
| `welding_carriage_clutch_lever_tip` | `welding_carriage_clutch_lever` | control |
| `welding_carriage_speed_knob_contact` | `welding_carriage_speed_knob` | control |

The URDF supplies geometry, articulation and frames. It does not model the drive motor, magnetic hold, weaving, track rail or the welding torch cable.
