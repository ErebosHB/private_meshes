# Portable Induction Heater

Hand-held induction heater lying flat, with a coil head that swivels on the neck, a trigger and a power dial.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block and neck rod plus a ring of boxes for the coil, so the coil opening stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `induction_heater_coil_head_joint` | revolute | 1.45 |
| `induction_heater_trigger_joint` | prismatic | 0.007 |
| `induction_heater_power_dial_joint` | revolute | 2.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `induction_heater_grip` | `induction_heater_body` | grasp |
| `induction_heater_trigger_contact` | `induction_heater_trigger` | control |
| `induction_heater_power_dial_contact` | `induction_heater_power_dial` | control |
| `induction_heater_coil_centre` | `induction_heater_coil_head` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the induction field, coil temperature, power electronics, cooling airflow or the heating of workpieces.
