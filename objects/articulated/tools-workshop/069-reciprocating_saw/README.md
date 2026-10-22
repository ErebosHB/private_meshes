# Reciprocating Saw

Sabre saw lying on its side, with a stroking blade plunger, a pivoting shoe, rear D-handle and trigger.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, handle bar, shoe and the blade, so the opening inside the rear handle stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `reciprocating_saw_plunger_joint` | prismatic | 0.028 |
| `reciprocating_saw_shoe_joint` | revolute | 0.42 |
| `reciprocating_saw_trigger_joint` | prismatic | 0.008 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `reciprocating_saw_rear_grip` | `reciprocating_saw_body` | grasp |
| `reciprocating_saw_front_boot_grip` | `reciprocating_saw_body` | grasp |
| `reciprocating_saw_trigger_contact` | `reciprocating_saw_trigger` | control |
| `reciprocating_saw_blade_tip` | `reciprocating_saw_plunger` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model stroke rate, the orbital action, blade clamping, vibration damping or cutting forces.
