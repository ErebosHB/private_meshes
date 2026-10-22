# Tumble Dryer

Front-loading dryer with a wide hinged porthole door, a pull-out condensate water tank and a program dial.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing panel and four strips around the porthole, so the drum and the water-tank housing stay open and reachable.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; glass 2,500; rubber 1,100; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `tumble_dryer_water_tank_joint` | prismatic | 0.26 |
| `tumble_dryer_program_dial_joint` | revolute | 1.57 |
| `tumble_dryer_start_button_joint` | prismatic | 0.003 |
| `tumble_dryer_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `tumble_dryer_water_tank_grip` | `tumble_dryer_water_tank` | grasp |
| `tumble_dryer_water_tank_volume` | `tumble_dryer_water_tank` | container_volume |
| `tumble_dryer_program_dial_contact` | `tumble_dryer_program_dial` | control |
| `tumble_dryer_start_button_contact` | `tumble_dryer_start_button` | control |
| `tumble_dryer_door_grip` | `tumble_dryer_door` | grasp |
| `tumble_dryer_drum_volume` | `tumble_dryer_body` | container_volume |
| `tumble_dryer_top_surface` | `tumble_dryer_body` | place_surface |
| `tumble_dryer_wall_anchor` | `tumble_dryer_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model heating, the heat pump, drum rotation, condensate flow, the door switch or load ratings.
