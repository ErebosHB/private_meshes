# Freestanding Cooker

Cooker with a four-zone glass-ceramic hob, an oven with drop-down door, a storage drawer and four hob dials.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing, frame and cavity panel, so the oven cavity and the storage drawer stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; glass 2,500; rubber 1,100; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `freestanding_cooker_rear_left_hob_dial_joint` | revolute | 1.57 |
| `freestanding_cooker_front_left_hob_dial_joint` | revolute | 1.57 |
| `freestanding_cooker_front_right_hob_dial_joint` | revolute | 1.57 |
| `freestanding_cooker_rear_right_hob_dial_joint` | revolute | 1.57 |
| `freestanding_cooker_storage_drawer_joint` | prismatic | 0.33 |
| `freestanding_cooker_oven_door_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `freestanding_cooker_rear_left_hob_dial_contact` | `freestanding_cooker_rear_left_hob_dial` | control |
| `freestanding_cooker_front_left_hob_dial_contact` | `freestanding_cooker_front_left_hob_dial` | control |
| `freestanding_cooker_front_right_hob_dial_contact` | `freestanding_cooker_front_right_hob_dial` | control |
| `freestanding_cooker_rear_right_hob_dial_contact` | `freestanding_cooker_rear_right_hob_dial` | control |
| `freestanding_cooker_storage_drawer_grip` | `freestanding_cooker_storage_drawer` | grasp |
| `freestanding_cooker_storage_drawer_volume` | `freestanding_cooker_storage_drawer` | container_volume |
| `freestanding_cooker_oven_door_grip` | `freestanding_cooker_oven_door` | grasp |
| `freestanding_cooker_oven_volume` | `freestanding_cooker_body` | container_volume |
| `freestanding_cooker_hob_surface` | `freestanding_cooker_body` | place_surface |
| `freestanding_cooker_wall_anchor` | `freestanding_cooker_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model hob or oven heating, residual-heat behaviour, the door's hinge springs, anti-tip fixing strength or load ratings.
