# Plunge Router

Router whose motor plunges down two guide columns toward an open base ring, with a depth rod, plunge lock and collet.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses a ring of boxes for the base and one primitive per column, sleeve, knob and the motor, so the bit opening stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `plunge_router_carriage_joint` | prismatic | 0.034 |
| `plunge_router_collet_joint` | continuous | 0.8 |
| `plunge_router_depth_rod_joint` | prismatic | 0.035 |
| `plunge_router_plunge_lock_joint` | revolute | 0.55 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `plunge_router_left_knob` | `plunge_router_carriage` | grasp |
| `plunge_router_right_knob` | `plunge_router_carriage` | grasp |
| `plunge_router_plunge_lock_contact` | `plunge_router_plunge_lock` | control |
| `plunge_router_depth_rod_knob` | `plunge_router_depth_rod` | control |
| `plunge_router_bit_tip` | `plunge_router_collet` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model spindle speed, plunge spring return, depth turret stops, bit runout, edge guides or dust extraction.
