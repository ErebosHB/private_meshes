# Dishwasher, Shallow Depth

Free-standing full-width dishwasher in a shallow cabinet, with a drop-down door, a push button and two pull-out racks.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing and tub panel and thin boxes for each rack's floor and walls, so the tub and both racks stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `dishwasher_shallow_door_joint` | revolute | 1.5 |
| `dishwasher_shallow_power_button_joint` | prismatic | 0.003 |
| `dishwasher_shallow_lower_rack_joint` | prismatic | 0.264 |
| `dishwasher_shallow_upper_rack_joint` | prismatic | 0.264 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `dishwasher_shallow_tub_volume` | `dishwasher_shallow_body` | container_volume |
| `dishwasher_shallow_door_grip` | `dishwasher_shallow_door` | grasp |
| `dishwasher_shallow_power_button_contact` | `dishwasher_shallow_power_button` | control |
| `dishwasher_shallow_lower_rack_grip` | `dishwasher_shallow_lower_rack` | grasp |
| `dishwasher_shallow_lower_rack_volume` | `dishwasher_shallow_lower_rack` | container_volume |
| `dishwasher_shallow_upper_rack_grip` | `dishwasher_shallow_upper_rack` | grasp |
| `dishwasher_shallow_upper_rack_volume` | `dishwasher_shallow_upper_rack` | container_volume |
| `dishwasher_shallow_top_surface` | `dishwasher_shallow_body` | place_surface |
| `dishwasher_shallow_wall_anchor` | `dishwasher_shallow_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model water supply, spray arms, the wash cycle, the door spring or load ratings.
