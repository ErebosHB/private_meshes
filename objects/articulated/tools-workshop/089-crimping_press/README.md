# Benchtop Crimping Press

Bench press for wire terminals with a ram that lowers the crimp tool onto the anvil, a hinged safety guard and a start button.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base, column, head, motor, anvil, ram and guard, so the crimp zone stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `crimping_press_ram_joint` | prismatic | 0.03 |
| `crimping_press_safety_guard_joint` | revolute | 1.2 |
| `crimping_press_start_button_joint` | prismatic | 0.004 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `crimping_press_safety_guard_grip` | `crimping_press_safety_guard` | grasp |
| `crimping_press_start_button_contact` | `crimping_press_start_button` | control |
| `crimping_press_crimp_tool` | `crimping_press_ram` | tool_attachment |
| `crimping_press_anvil_surface` | `crimping_press_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model the press motor, crimp force monitoring, terminal feed, applicator tooling or the guard interlock.
