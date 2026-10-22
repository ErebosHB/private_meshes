# Stud Welding Gun

Pistol-type stud welding gun lying on its side, with telescoping support legs, a spring-loaded stud chuck and a trigger.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level under the barrel, with the gun lying on its side.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per barrel, handle, leg and cable segment, with boxes around the leg sleeves so they stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `stud_welding_gun_support_legs_joint` | prismatic | 0.05 |
| `stud_welding_gun_stud_chuck_joint` | prismatic | 0.012 |
| `stud_welding_gun_trigger_joint` | revolute | 0.28 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `stud_welding_gun_handle_grip` | `stud_welding_gun_body` | grasp |
| `stud_welding_gun_trigger_contact` | `stud_welding_gun_trigger` | control |
| `stud_welding_gun_stud_tip` | `stud_welding_gun_stud_chuck` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the lift solenoid, arc, plunge spring, ferrules or weld timing.
