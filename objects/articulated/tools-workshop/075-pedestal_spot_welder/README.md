# Pedestal Spot Welder

Floor-standing resistance spot welder with a rocker arm that lifts the upper electrode, a foot pedal, a heat knob and a side service door.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per cabinet wall, plinth and pedal plate plus cylinders for the horns and electrodes, so the service bay stays open behind the door.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `pedestal_spot_welder_rocker_arm_joint` | revolute | 0.2 |
| `pedestal_spot_welder_service_door_joint` | revolute | 1.4 |
| `pedestal_spot_welder_foot_pedal_joint` | revolute | 0.25 |
| `pedestal_spot_welder_heat_knob_joint` | revolute | 2.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `pedestal_spot_welder_foot_pedal_contact` | `pedestal_spot_welder_foot_pedal` | control |
| `pedestal_spot_welder_heat_knob_contact` | `pedestal_spot_welder_heat_knob` | control |
| `pedestal_spot_welder_service_door_grip` | `pedestal_spot_welder_service_door` | grasp |
| `pedestal_spot_welder_upper_electrode_tip` | `pedestal_spot_welder_rocker_arm` | tool_attachment |
| `pedestal_spot_welder_lower_electrode_tip` | `pedestal_spot_welder_body` | tool_attachment |
| `pedestal_spot_welder_rear_anchor` | `pedestal_spot_welder_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the welding transformer, electrode force, cooling water, weld timing or the pedal switch.
