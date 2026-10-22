# Suspension-File Drawer Cabinet

Sheet-steel cabinet with four full-extension drawers for hanging files.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per sheet-steel wall and drawer wall, so every drawer stays open as a container.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `suspension_file_cabinet_drawer_1_joint` | prismatic | 0.33 |
| `suspension_file_cabinet_drawer_2_joint` | prismatic | 0.33 |
| `suspension_file_cabinet_drawer_3_joint` | prismatic | 0.33 |
| `suspension_file_cabinet_drawer_4_joint` | prismatic | 0.33 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `suspension_file_cabinet_drawer_1_grip` | `suspension_file_cabinet_drawer_1` | grasp |
| `suspension_file_cabinet_drawer_1_volume` | `suspension_file_cabinet_drawer_1` | container_volume |
| `suspension_file_cabinet_drawer_2_grip` | `suspension_file_cabinet_drawer_2` | grasp |
| `suspension_file_cabinet_drawer_2_volume` | `suspension_file_cabinet_drawer_2` | container_volume |
| `suspension_file_cabinet_drawer_3_grip` | `suspension_file_cabinet_drawer_3` | grasp |
| `suspension_file_cabinet_drawer_3_volume` | `suspension_file_cabinet_drawer_3` | container_volume |
| `suspension_file_cabinet_drawer_4_grip` | `suspension_file_cabinet_drawer_4` | grasp |
| `suspension_file_cabinet_drawer_4_volume` | `suspension_file_cabinet_drawer_4` | container_volume |
| `suspension_file_cabinet_top_surface` | `suspension_file_cabinet_body` | place_surface |
| `suspension_file_cabinet_wall_anchor` | `suspension_file_cabinet_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model drawer runners, the interlock that lets only one drawer open, locks, load ratings or tip-over behaviour.
