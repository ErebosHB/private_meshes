# Mobile Drawer Pedestal

Under-desk pedestal on four castors with a stationery drawer and two deep drawers.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel and drawer wall, so every drawer stays open as a container.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `mobile_pedestal_castor_1_joint` | continuous | 0 |
| `mobile_pedestal_castor_2_joint` | continuous | 0 |
| `mobile_pedestal_castor_3_joint` | continuous | 0 |
| `mobile_pedestal_castor_4_joint` | continuous | 0 |
| `mobile_pedestal_drawer_1_joint` | prismatic | 0.3 |
| `mobile_pedestal_drawer_2_joint` | prismatic | 0.3 |
| `mobile_pedestal_drawer_3_joint` | prismatic | 0.3 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `mobile_pedestal_drawer_1_grip` | `mobile_pedestal_drawer_1` | grasp |
| `mobile_pedestal_drawer_1_volume` | `mobile_pedestal_drawer_1` | container_volume |
| `mobile_pedestal_drawer_2_grip` | `mobile_pedestal_drawer_2` | grasp |
| `mobile_pedestal_drawer_2_volume` | `mobile_pedestal_drawer_2` | container_volume |
| `mobile_pedestal_drawer_3_grip` | `mobile_pedestal_drawer_3` | grasp |
| `mobile_pedestal_drawer_3_volume` | `mobile_pedestal_drawer_3` | container_volume |
| `mobile_pedestal_top_surface` | `mobile_pedestal_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model drawer runners, central locking, castor brakes or swivel, load ratings or tip-over behaviour.
