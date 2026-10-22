# Freestanding Dishwasher

Full-size dishwasher with a drop-down door, two pull-out wire racks and a rotating lower spray arm.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing and tub panel and thin boxes for each rack's floor and walls, so the tub and both racks stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; rubber 1,100; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `dishwasher_spray_arm_joint` | continuous | 0 |
| `dishwasher_lower_rack_joint` | prismatic | 0.317 |
| `dishwasher_upper_rack_joint` | prismatic | 0.317 |
| `dishwasher_door_joint` | revolute | 1.5 |
| `dishwasher_power_button_joint` | prismatic | 0.003 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `dishwasher_lower_rack_grip` | `dishwasher_lower_rack` | grasp |
| `dishwasher_lower_rack_volume` | `dishwasher_lower_rack` | container_volume |
| `dishwasher_upper_rack_grip` | `dishwasher_upper_rack` | grasp |
| `dishwasher_upper_rack_volume` | `dishwasher_upper_rack` | container_volume |
| `dishwasher_power_button_contact` | `dishwasher_power_button` | control |
| `dishwasher_door_grip` | `dishwasher_door` | grasp |
| `dishwasher_tub_volume` | `dishwasher_body` | container_volume |
| `dishwasher_top_surface` | `dishwasher_body` | place_surface |
| `dishwasher_wall_anchor` | `dishwasher_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model water, pumps, heating, the spray pattern, door springs or load ratings; the door's inspection angle is set near horizontal so the racks clear it.
