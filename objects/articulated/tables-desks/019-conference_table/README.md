# Conference Table with Cable Well

Meeting table for six with a hinged cable-well lid and an open cable tray below.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses four boxes around the cable opening and one per tray wall, so the well and tray stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `conference_table_cable_lid_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `conference_table_cable_lid_grip` | `conference_table_cable_lid` | grasp |
| `conference_table_cable_tray_volume` | `conference_table_body` | container_volume |
| `conference_table_tabletop_left_surface` | `conference_table_body` | place_surface |
| `conference_table_tabletop_right_surface` | `conference_table_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model power sockets, cable routing, load ratings or the lid's friction hinge.
