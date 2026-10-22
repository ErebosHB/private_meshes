# Diamond Core Drill Rig

Core drilling motor on a column stand, fed down by a three-spoke lever, over a U-shaped base plate.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per base rail, column and carriage block plus a ring of boxes for the core bit, so the bore and the base opening stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `diamond_core_drill_rig_carriage_joint` | prismatic | 0.24 |
| `diamond_core_drill_rig_motor_switch_joint` | prismatic | 0.004 |
| `diamond_core_drill_rig_feed_lever_joint` | revolute | 2.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `diamond_core_drill_rig_feed_lever_knob` | `diamond_core_drill_rig_feed_lever` | grasp |
| `diamond_core_drill_rig_motor_handle_grip` | `diamond_core_drill_rig_carriage` | grasp |
| `diamond_core_drill_rig_motor_switch_contact` | `diamond_core_drill_rig_motor_switch` | control |
| `diamond_core_drill_rig_core_bit_crown` | `diamond_core_drill_rig_carriage` | tool_attachment |
| `diamond_core_drill_rig_base_plate_surface` | `diamond_core_drill_rig_body` | place_surface |
| `diamond_core_drill_rig_column_anchor` | `diamond_core_drill_rig_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model drilling torque, water flushing, the slip clutch, anchoring or vacuum fixing of the base, core extraction or tip-over behaviour.
