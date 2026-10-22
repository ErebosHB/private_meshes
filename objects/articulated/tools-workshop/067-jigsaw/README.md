# Jigsaw

Top-handle jigsaw on a flat shoe; the body tilts for bevel cuts, the blade plunger strokes, with a pendulum lever and speed wheel.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per shoe, housing block, handle bar and the blade, so the opening inside the top handle stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `jigsaw_body_unit_joint` | revolute | 0.5 |
| `jigsaw_plunger_joint` | prismatic | 0.022 |
| `jigsaw_pendulum_lever_joint` | revolute | 0.85 |
| `jigsaw_speed_wheel_joint` | revolute | 2 |
| `jigsaw_trigger_joint` | prismatic | 0.007 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `jigsaw_top_grip` | `jigsaw_body_unit` | grasp |
| `jigsaw_pendulum_lever_tip` | `jigsaw_pendulum_lever` | control |
| `jigsaw_speed_wheel_contact` | `jigsaw_speed_wheel` | control |
| `jigsaw_trigger_contact` | `jigsaw_trigger` | control |
| `jigsaw_blade_tip` | `jigsaw_plunger` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the pendulum orbit, stroke rate, blade guidance roller, splinter guard, dust blowing or cutting forces.
