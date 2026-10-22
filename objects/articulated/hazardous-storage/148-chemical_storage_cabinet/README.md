# Chemical Cabinet with Pull-out Trays

Sheet-steel cabinet for aggressive or polluting liquids: two hinged doors over three pull-out sump trays and a fixed floor sump.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per wall, door leaf and tray wall, so every tray and the floor sump stay open from above.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; hollow steel profiles as an equivalent 1,900; ABS/HDPE 1,050 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `chemical_storage_cabinet_tray_1_joint` | prismatic | 0.24 |
| `chemical_storage_cabinet_tray_2_joint` | prismatic | 0.24 |
| `chemical_storage_cabinet_tray_3_joint` | prismatic | 0.24 |
| `chemical_storage_cabinet_left_door_joint` | revolute | 1.4 |
| `chemical_storage_cabinet_right_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `chemical_storage_cabinet_floor_sump_volume` | `chemical_storage_cabinet_body` | container_volume |
| `chemical_storage_cabinet_wall_anchor` | `chemical_storage_cabinet_body` | wall_mount |
| `chemical_storage_cabinet_tray_1_grip` | `chemical_storage_cabinet_tray_1` | grasp |
| `chemical_storage_cabinet_tray_1_volume` | `chemical_storage_cabinet_tray_1` | container_volume |
| `chemical_storage_cabinet_tray_2_grip` | `chemical_storage_cabinet_tray_2` | grasp |
| `chemical_storage_cabinet_tray_2_volume` | `chemical_storage_cabinet_tray_2` | container_volume |
| `chemical_storage_cabinet_tray_3_grip` | `chemical_storage_cabinet_tray_3` | grasp |
| `chemical_storage_cabinet_tray_3_volume` | `chemical_storage_cabinet_tray_3` | container_volume |
| `chemical_storage_cabinet_left_door_grip` | `chemical_storage_cabinet_left_door` | grasp |
| `chemical_storage_cabinet_right_door_grip` | `chemical_storage_cabinet_right_door` | grasp |

The URDF supplies geometry, articulation and frames. It does not model chemical resistance of the coating, ventilation, tray runners and end stops, liquid retention or load ratings.
