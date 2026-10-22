# Wire Feeder

Separate wire-feed case on skids with a windowed side door over the spool bay, a hinged pressure arm on the drive rolls and a speed knob.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per case wall and skid plus cylinders for the spool, rolls and handle, so the spool bay stays open behind the door.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wire_feeder_side_door_joint` | revolute | 1.4 |
| `wire_feeder_wire_spool_joint` | continuous | 0 |
| `wire_feeder_pressure_arm_joint` | revolute | 0.9 |
| `wire_feeder_wire_speed_knob_joint` | revolute | 2.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wire_feeder_side_door_grip` | `wire_feeder_side_door` | grasp |
| `wire_feeder_carry_handle_grip` | `wire_feeder_body` | grasp |
| `wire_feeder_wire_speed_knob_contact` | `wire_feeder_wire_speed_knob` | control |
| `wire_feeder_pressure_arm_tip` | `wire_feeder_pressure_arm` | control |
| `wire_feeder_spool_bay_volume` | `wire_feeder_body` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model the feed motor, roll pressure, wire, gas valve or the interconnection cable.
