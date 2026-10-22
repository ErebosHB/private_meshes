# Magnetic Core Drill

Drill on an electromagnetic base whose motor slides down the column via a three-spoke feed handle, with an annular cutter.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base, column, slide and motor part plus a ring of boxes for the cutter, so its bore stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `magnetic_core_drill_motor_slide_joint` | prismatic | 0.06 |
| `magnetic_core_drill_motor_switch_joint` | revolute | 0.4 |
| `magnetic_core_drill_arbor_joint` | continuous | 0.9 |
| `magnetic_core_drill_feed_handle_joint` | revolute | 1.8 |
| `magnetic_core_drill_magnet_switch_joint` | revolute | 1.57 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `magnetic_core_drill_carry_handle_grip` | `magnetic_core_drill_body` | grasp |
| `magnetic_core_drill_feed_handle_knob` | `magnetic_core_drill_feed_handle` | grasp |
| `magnetic_core_drill_magnet_switch_contact` | `magnetic_core_drill_magnet_switch` | control |
| `magnetic_core_drill_motor_switch_contact` | `magnetic_core_drill_motor_switch` | control |
| `magnetic_core_drill_cutter_teeth` | `magnetic_core_drill_arbor` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model magnetic holding force, the safety strap, cutting coolant, motor overload protection or slug ejection.
