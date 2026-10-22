# Desktop Dispensing Robot

Three-axis benchtop gantry for glue dots and beads: the table slides front to back, the carriage across and the syringe head up and down.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per base, column, beam, table, carriage and head part plus cylinders for the syringe, so the work area stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `desktop_dispensing_robot_y_table_joint` | prismatic | 0.12 |
| `desktop_dispensing_robot_x_carriage_joint` | prismatic | 0.1 |
| `desktop_dispensing_robot_z_head_joint` | prismatic | 0.07 |
| `desktop_dispensing_robot_emergency_stop_joint` | prismatic | 0.006 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `desktop_dispensing_robot_table_surface` | `desktop_dispensing_robot_y_table` | place_surface |
| `desktop_dispensing_robot_needle_tip` | `desktop_dispensing_robot_z_head` | tool_attachment |
| `desktop_dispensing_robot_emergency_stop_contact` | `desktop_dispensing_robot_emergency_stop` | control |

The URDF supplies geometry, articulation and frames. It does not model the stepper drives, dispensing pressure, fluid, teach programs or the controller.
