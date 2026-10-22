# Walk-in Storage Container

Ten-foot steel storage container with corrugated walls and two end doors, each locked by a swinging bar handle.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per frame member, wall panel, floor and door leaf, so the interior stays open behind the doors.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; hollow steel profiles as an equivalent 1,900; ABS/HDPE 1,050; particleboard 650 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `storage_container_left_door_joint` | revolute | 1.4 |
| `storage_container_left_door_lever_joint` | revolute | 1.4 |
| `storage_container_right_door_joint` | revolute | 1.4 |
| `storage_container_right_door_lever_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `storage_container_interior_volume` | `storage_container_body` | container_volume |
| `storage_container_floor_surface` | `storage_container_body` | place_surface |
| `storage_container_corner_casting_anchor` | `storage_container_body` | wall_mount |
| `storage_container_left_door_edge_grip` | `storage_container_left_door` | grasp |
| `storage_container_left_door_lever_tip` | `storage_container_left_door_lever` | control |
| `storage_container_right_door_edge_grip` | `storage_container_right_door` | grasp |
| `storage_container_right_door_lever_tip` | `storage_container_right_door_lever` | control |

The URDF supplies geometry, articulation and frames. It does not model door seals, cam locks on the locking bars, corrugation stiffness, lifting loads at the corner castings, ventilation or load ratings.
