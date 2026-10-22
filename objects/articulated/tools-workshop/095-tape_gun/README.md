# Handheld Tape Gun

Carton-sealing tape dispenser standing upright: the tape roll turns on its hub, the blade guard flips open and a knob sets the hub tension.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes around the tape roll and one primitive per frame plate, handle, roller and guard, so the roll core stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `tape_gun_tape_hub_joint` | continuous | 0 |
| `tape_gun_blade_guard_joint` | revolute | 1 |
| `tape_gun_tension_knob_joint` | revolute | 2.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `tape_gun_handle_grip` | `tape_gun_body` | grasp |
| `tape_gun_tape_roll_mount` | `tape_gun_body` | tool_attachment |
| `tape_gun_blade_guard_grip` | `tape_gun_blade_guard` | grasp |
| `tape_gun_tension_knob_contact` | `tape_gun_tension_knob` | control |

The URDF supplies geometry, articulation and frames. It does not model tape adhesion, unwinding drag, blade cutting or the guard spring.
