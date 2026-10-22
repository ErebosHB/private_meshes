# MIG/MAG Welding Machine on Trolley

Wheeled wire-feed welding machine with a hinged side door over the wire-spool bay, two front control knobs and a rear push handle.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing wall and trolley plate plus cylinders for wheels and handle, so the spool bay stays open behind the side door.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `trolley_mig_welder_side_door_joint` | revolute | 1.4 |
| `trolley_mig_welder_wire_spool_joint` | continuous | 0 |
| `trolley_mig_welder_voltage_knob_joint` | revolute | 2.4 |
| `trolley_mig_welder_wire_speed_knob_joint` | revolute | 2.4 |
| `trolley_mig_welder_left_rear_wheel_joint` | continuous | 0 |
| `trolley_mig_welder_right_rear_wheel_joint` | continuous | 0 |
| `trolley_mig_welder_left_front_castor_joint` | continuous | 0 |
| `trolley_mig_welder_right_front_castor_joint` | continuous | 0 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `trolley_mig_welder_side_door_grip` | `trolley_mig_welder_side_door` | grasp |
| `trolley_mig_welder_voltage_knob_contact` | `trolley_mig_welder_voltage_knob` | control |
| `trolley_mig_welder_wire_speed_knob_contact` | `trolley_mig_welder_wire_speed_knob` | control |
| `trolley_mig_welder_push_handle_grip` | `trolley_mig_welder_body` | grasp |
| `trolley_mig_welder_spool_bay_volume` | `trolley_mig_welder_body` | container_volume |
| `trolley_mig_welder_top_surface` | `trolley_mig_welder_body` | place_surface |
| `trolley_mig_welder_tether_anchor` | `trolley_mig_welder_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the welding power source, wire-feed motor, gas flow, castor swivel, torch cable or tip-over behaviour.
