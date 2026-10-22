# Wet/Dry Workshop Vacuum

Drum vacuum on a wheeled base whose motor head unlatches and lifts off the tank, with a front hose inlet and a power knob.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses a ring of boxes for the tank wall and one primitive per wheel, latch and head part, so the tank stays open when the head is lifted.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wet_dry_vacuum_wheel_1_joint` | continuous | 0 |
| `wet_dry_vacuum_wheel_2_joint` | continuous | 0 |
| `wet_dry_vacuum_wheel_3_joint` | continuous | 0 |
| `wet_dry_vacuum_wheel_4_joint` | continuous | 0 |
| `wet_dry_vacuum_head_joint` | prismatic | 0.17 |
| `wet_dry_vacuum_power_knob_joint` | revolute | 1.57 |
| `wet_dry_vacuum_left_latch_joint` | revolute | 1.25 |
| `wet_dry_vacuum_right_latch_joint` | revolute | 1.25 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wet_dry_vacuum_left_latch_grip` | `wet_dry_vacuum_left_latch` | grasp |
| `wet_dry_vacuum_right_latch_grip` | `wet_dry_vacuum_right_latch` | grasp |
| `wet_dry_vacuum_carry_grip` | `wet_dry_vacuum_head` | grasp |
| `wet_dry_vacuum_power_knob_contact` | `wet_dry_vacuum_power_knob` | control |
| `wet_dry_vacuum_tank_volume` | `wet_dry_vacuum_body` | container_volume |
| `wet_dry_vacuum_hose_inlet` | `wet_dry_vacuum_body` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model suction power, the filter cleaning pulse, the float shut-off, hose flexibility, castor swivel or tip-over behaviour.
