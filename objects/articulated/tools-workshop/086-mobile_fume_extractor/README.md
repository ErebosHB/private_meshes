# Mobile Fume Extractor

Filter unit on castors with a front door over two filter cartridges, a pull-out dust tray, a power rocker and a hose collar on top.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per cabinet wall, tray wall and castor fork plus cylinders for the cartridges and collar, so the filter bay and tray stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `mobile_fume_extractor_filter_door_joint` | revolute | 1.4 |
| `mobile_fume_extractor_dust_tray_joint` | prismatic | 0.24 |
| `mobile_fume_extractor_power_switch_joint` | revolute | 0.3 |
| `mobile_fume_extractor_castor_1_joint` | continuous | 0 |
| `mobile_fume_extractor_castor_2_joint` | continuous | 0 |
| `mobile_fume_extractor_castor_3_joint` | continuous | 0 |
| `mobile_fume_extractor_castor_4_joint` | continuous | 0 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `mobile_fume_extractor_push_handle_grip` | `mobile_fume_extractor_body` | grasp |
| `mobile_fume_extractor_filter_door_grip` | `mobile_fume_extractor_filter_door` | grasp |
| `mobile_fume_extractor_dust_tray_grip` | `mobile_fume_extractor_dust_tray` | grasp |
| `mobile_fume_extractor_dust_tray_volume` | `mobile_fume_extractor_dust_tray` | container_volume |
| `mobile_fume_extractor_power_switch_contact` | `mobile_fume_extractor_power_switch` | control |
| `mobile_fume_extractor_hose_collar` | `mobile_fume_extractor_body` | tool_attachment |
| `mobile_fume_extractor_rear_anchor` | `mobile_fume_extractor_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the fan, airflow, filter loading, filter cleaning or the extraction hose.
