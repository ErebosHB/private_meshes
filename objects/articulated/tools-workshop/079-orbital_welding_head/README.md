# Orbital Welding Head

Closed tube-welding head on a hand grip: a hinged clamp jaw, a latch lever and a rotor ring that carries the electrode around the bore.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per clamshell block and eight boxes around the rotor ring, so the tube bore stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `orbital_welding_head_clamp_jaw_joint` | revolute | 1.3 |
| `orbital_welding_head_rotor_ring_joint` | continuous | 1.2 |
| `orbital_welding_head_clamp_lever_joint` | revolute | 1 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `orbital_welding_head_handle_grip` | `orbital_welding_head_body` | grasp |
| `orbital_welding_head_clamp_lever_tip` | `orbital_welding_head_clamp_lever` | control |
| `orbital_welding_head_electrode` | `orbital_welding_head_rotor_ring` | tool_attachment |
| `orbital_welding_head_tube_bore_volume` | `orbital_welding_head_body` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model the rotor drive, arc, gas purge, water cooling or tube clamping force.
