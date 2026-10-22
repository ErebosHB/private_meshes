# Tilting Welding Positioner

Benchtop positioner whose slotted turntable rotates and tilts forward on trunnions, with a speed knob on the base.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base, cheek, trunnion, cradle, turntable and clamp block.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `welding_positioner_tilt_cradle_joint` | revolute | 1.2 |
| `welding_positioner_turntable_joint` | continuous | 0.8 |
| `welding_positioner_speed_knob_joint` | revolute | 2.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `welding_positioner_turntable_surface` | `welding_positioner_turntable` | place_surface |
| `welding_positioner_fixture_mount` | `welding_positioner_turntable` | tool_attachment |
| `welding_positioner_speed_knob_contact` | `welding_positioner_speed_knob` | control |

The URDF supplies geometry, articulation and frames. It does not model the gear drives, load and torque ratings, earth return through the table or the foot switch.
