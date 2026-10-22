# Countertop Microwave

Countertop microwave with a side-hinged window door, a glass turntable and two control dials.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing and cavity panel and a disc for the turntable, so the cavity stays open behind the door.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; glass 2,500; rubber 1,100 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `microwave_turntable_joint` | continuous | 0 |
| `microwave_power_dial_joint` | revolute | 1.57 |
| `microwave_timer_dial_joint` | revolute | 1.57 |
| `microwave_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `microwave_turntable_surface` | `microwave_turntable` | place_surface |
| `microwave_power_dial_contact` | `microwave_power_dial` | control |
| `microwave_timer_dial_contact` | `microwave_timer_dial` | control |
| `microwave_door_grip` | `microwave_door` | grasp |
| `microwave_cavity_volume` | `microwave_body` | container_volume |
| `microwave_top_surface` | `microwave_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model microwave heating, the turntable motor, the door interlock or load ratings.
