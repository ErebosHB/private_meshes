# Mobile Platform Steps

Four-step steel platform steps with handrails, a self-closing gate at the top and two rear castors for moving it.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per stringer, leg, tread, rail and castor, so the stair opening and the platform stay clear.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (hollow steel profiles as an equivalent 1,900; steel grating as an equivalent 1,500; ABS/HDPE 1,050; rubber 1,200 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `mobile_platform_steps_gate_joint` | revolute | 1.4 |
| `mobile_platform_steps_left_castor_joint` | continuous | 0 |
| `mobile_platform_steps_right_castor_joint` | continuous | 0 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `mobile_platform_steps_left_handrail_grip` | `mobile_platform_steps_body` | grasp |
| `mobile_platform_steps_right_handrail_grip` | `mobile_platform_steps_body` | grasp |
| `mobile_platform_steps_platform_surface` | `mobile_platform_steps_body` | place_surface |
| `mobile_platform_steps_anti_tip_anchor` | `mobile_platform_steps_body` | wall_mount |
| `mobile_platform_steps_gate_grip` | `mobile_platform_steps_gate` | grasp |

The URDF supplies geometry, articulation and frames. It does not model the gate return spring, spring-loaded castor retraction, anti-slip tread texture, load ratings or tip-over behaviour.
