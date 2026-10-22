# Front-Load Washing Machine

Front-loading washer with a hinged porthole door, a pull-out detergent drawer and a program dial.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing panel and four strips around the porthole, so the drum, detergent drawer and its housing stay open and reachable.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; glass 2,500; rubber 1,100; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `washing_machine_detergent_drawer_joint` | prismatic | 0.22 |
| `washing_machine_program_dial_joint` | revolute | 1.57 |
| `washing_machine_start_button_joint` | prismatic | 0.003 |
| `washing_machine_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `washing_machine_detergent_drawer_grip` | `washing_machine_detergent_drawer` | grasp |
| `washing_machine_detergent_drawer_volume` | `washing_machine_detergent_drawer` | container_volume |
| `washing_machine_program_dial_contact` | `washing_machine_program_dial` | control |
| `washing_machine_start_button_contact` | `washing_machine_start_button` | control |
| `washing_machine_door_grip` | `washing_machine_door` | grasp |
| `washing_machine_drum_volume` | `washing_machine_body` | container_volume |
| `washing_machine_top_surface` | `washing_machine_body` | place_surface |
| `washing_machine_wall_anchor` | `washing_machine_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the motor, drum rotation, water, the door lock, spin vibration or load ratings.
