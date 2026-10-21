# Robot Charging Dock

Wall-standing charging dock for a mobile robot with two spring-loaded contact pads behind a floor plate.

Original concept model by Vanessa Hassouna, developed for AICOR Solutions.
Typology drawn from a public product reference; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint; the robot docks from the negative Y side.
Use a unique URDF parser prefix for each instance.
Collision uses boxes for the housing, the floor plate and each contact pad.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `charging_dock_left_pad_joint` | prismatic | 0.01 |
| `charging_dock_right_pad_joint` | prismatic | 0.01 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `charging_dock_wall_anchor` | `charging_dock_body` | wall_mount |
| `charging_dock_left_contact` | `charging_dock_left_pad` | control |
| `charging_dock_right_contact` | `charging_dock_right_pad` | control |

The URDF supplies geometry, articulation and frames. It does not model charging, contact detection, the robot's docking behaviour or any power electronics.
