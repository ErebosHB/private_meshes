# Mitre Saw

Bench mitre saw: the turntable swings for mitre angles, the saw arm pivots down, the lower guard retracts and the blade spins.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base, fence, turntable, arm and guard part, so the kerf slot and the gap under the raised arm stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `mitre_saw_turntable_joint` | revolute | 0.55 |
| `mitre_saw_saw_arm_joint` | revolute | 0.5 |
| `mitre_saw_blade_joint` | continuous | 0 |
| `mitre_saw_lower_guard_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `mitre_saw_d_handle_grip` | `mitre_saw_saw_arm` | grasp |
| `mitre_saw_lock_handle_grip` | `mitre_saw_turntable` | grasp |
| `mitre_saw_left_table_surface` | `mitre_saw_body` | place_surface |
| `mitre_saw_right_table_surface` | `mitre_saw_body` | place_surface |
| `mitre_saw_blade_edge` | `mitre_saw_blade` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the arm's return spring, blade brake, laser guide, bevel tilt, clamping, dust extraction or cutting forces.
