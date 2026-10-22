# Automatic Screwdriving Unit

Column-mounted screwdriving spindle on a work table: the spindle carriage lowers on the column, the bit turns, and a toggle clamp holds the part.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base, table, column, carriage, spindle and clamp part, so the space under the spindle stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `screwdriving_unit_spindle_carriage_joint` | prismatic | 0.22 |
| `screwdriving_unit_spindle_joint` | continuous | 0 |
| `screwdriving_unit_clamp_lever_joint` | revolute | 1 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `screwdriving_unit_bit_tip` | `screwdriving_unit_spindle` | tool_attachment |
| `screwdriving_unit_work_table_surface` | `screwdriving_unit_body` | place_surface |
| `screwdriving_unit_clamp_lever_grip` | `screwdriving_unit_clamp_lever` | control |
| `screwdriving_unit_column_anchor` | `screwdriving_unit_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the screwdriving motor, torque control, screw feeding, vacuum pick-up or the cable.
