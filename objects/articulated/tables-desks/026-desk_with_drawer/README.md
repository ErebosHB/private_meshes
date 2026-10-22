# Desk with Drawer and Cable Flap

Panel-leg writing desk with a shallow under-top drawer and a hinged cable flap.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, tray wall and the four desktop pieces around the cable opening.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `desk_with_drawer_drawer_joint` | prismatic | 0.264 |
| `desk_with_drawer_cable_flap_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `desk_with_drawer_drawer_grip` | `desk_with_drawer_drawer` | grasp |
| `desk_with_drawer_drawer_volume` | `desk_with_drawer_drawer` | container_volume |
| `desk_with_drawer_cable_flap_grip` | `desk_with_drawer_cable_flap` | grasp |
| `desk_with_drawer_cable_tray_volume` | `desk_with_drawer_body` | container_volume |
| `desk_with_drawer_desktop_surface` | `desk_with_drawer_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model drawer runners, cable routing, levelling feet, load ratings or the flap's friction hinge.
