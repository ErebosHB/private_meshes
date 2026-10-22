# Circular Saw

Hand circular saw on a flat base plate; the saw unit tilts for bevel cuts, the lower blade guard swings back and the blade spins.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base plate, housing block, guard and the blade, so the gap between blade and guards stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `circular_saw_saw_unit_joint` | revolute | 0.55 |
| `circular_saw_blade_joint` | continuous | 0.6 |
| `circular_saw_lower_guard_joint` | revolute | 1.35 |
| `circular_saw_trigger_joint` | prismatic | 0.008 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `circular_saw_rear_grip` | `circular_saw_saw_unit` | grasp |
| `circular_saw_front_knob_grip` | `circular_saw_saw_unit` | grasp |
| `circular_saw_guard_lever_tip` | `circular_saw_lower_guard` | control |
| `circular_saw_trigger_contact` | `circular_saw_trigger` | control |
| `circular_saw_blade_edge` | `circular_saw_blade` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model cutting depth adjustment, the riving knife, blade brake, kickback, dust extraction or the guard's return spring.
