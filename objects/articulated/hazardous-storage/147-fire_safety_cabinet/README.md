# Fire-Resistant Safety Cabinet

Insulated two-door cabinet for flammable liquids with three shelf trays and a bottom sump.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per insulated wall, door leaf, shelf tray and sump wall, so the compartment stays open behind the doors.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; insulated steel wall panels as an equivalent 1,100; ABS/HDPE 1,050 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `fire_safety_cabinet_left_door_joint` | revolute | 1.4 |
| `fire_safety_cabinet_right_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `fire_safety_cabinet_shelf_1_surface` | `fire_safety_cabinet_body` | place_surface |
| `fire_safety_cabinet_shelf_2_surface` | `fire_safety_cabinet_body` | place_surface |
| `fire_safety_cabinet_shelf_3_surface` | `fire_safety_cabinet_body` | place_surface |
| `fire_safety_cabinet_sump_volume` | `fire_safety_cabinet_body` | container_volume |
| `fire_safety_cabinet_wall_anchor` | `fire_safety_cabinet_body` | wall_mount |
| `fire_safety_cabinet_left_door_grip` | `fire_safety_cabinet_left_door` | grasp |
| `fire_safety_cabinet_right_door_grip` | `fire_safety_cabinet_right_door` | grasp |

The URDF supplies geometry, articulation and frames. It does not model fire resistance, the door closers and thermal release, ventilation ducts, earthing, liquid retention or load ratings.
