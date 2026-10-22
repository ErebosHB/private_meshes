# Hazardous Materials Depot

Outdoor steel depot with an integrated floor sump under a grating and two wing doors, the right one locked by a swing handle.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per wall, roof, door leaf and sump wall plus a slab for the floor grating, so the interior stays open behind the doors.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; hollow steel profiles as an equivalent 1,900; steel grating as an equivalent 1,500; ABS/HDPE 1,050 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `hazmat_depot_left_door_joint` | revolute | 1.4 |
| `hazmat_depot_right_door_joint` | revolute | 1.4 |
| `hazmat_depot_right_door_handle_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `hazmat_depot_depot_volume` | `hazmat_depot_body` | container_volume |
| `hazmat_depot_floor_grating_surface` | `hazmat_depot_body` | place_surface |
| `hazmat_depot_floor_anchor` | `hazmat_depot_body` | wall_mount |
| `hazmat_depot_left_door_grip` | `hazmat_depot_left_door` | grasp |
| `hazmat_depot_right_door_grip` | `hazmat_depot_right_door` | grasp |
| `hazmat_depot_right_door_handle_tip` | `hazmat_depot_right_door_handle` | control |

The URDF supplies geometry, articulation and frames. It does not model fire resistance, ventilation, earthing, liquid retention of the sump, snow and wind loads, anchoring strength or load ratings.
