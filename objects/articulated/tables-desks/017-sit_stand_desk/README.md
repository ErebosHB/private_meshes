# Electric Sit-Stand Desk

Desk on two telescoping columns with a front control pad for raising and lowering the top.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per foot, column, rail and the desktop.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `sit_stand_desk_lift_joint` | prismatic | 0.4 |
| `sit_stand_desk_lift_button_joint` | prismatic | 0.004 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `sit_stand_desk_lift_button_contact` | `sit_stand_desk_lift_button` | control |
| `sit_stand_desk_desktop_surface` | `sit_stand_desk_lift` | place_surface |
| `sit_stand_desk_desktop_front_grip` | `sit_stand_desk_lift` | grasp |

The URDF supplies geometry, articulation and frames. It does not model the lift motors, collision stop, memory positions, load ratings or the cable chain.
