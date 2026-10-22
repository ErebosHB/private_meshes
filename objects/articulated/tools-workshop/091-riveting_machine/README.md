# Benchtop Riveting Machine

C-frame radial riveting machine: the quill lowers the spinning peen onto the anvil behind a hinged finger guard, started with two hand buttons.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base, column, head, motor, anvil, quill and guard, so the riveting zone stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `riveting_machine_quill_joint` | prismatic | 0.14 |
| `riveting_machine_peen_spindle_joint` | continuous | 0 |
| `riveting_machine_finger_guard_joint` | revolute | 1 |
| `riveting_machine_left_button_joint` | prismatic | 0.005 |
| `riveting_machine_right_button_joint` | prismatic | 0.005 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `riveting_machine_left_button_contact` | `riveting_machine_left_button` | control |
| `riveting_machine_right_button_contact` | `riveting_machine_right_button` | control |
| `riveting_machine_peen_tip` | `riveting_machine_peen_spindle` | tool_attachment |
| `riveting_machine_anvil_surface` | `riveting_machine_body` | place_surface |
| `riveting_machine_finger_guard_grip` | `riveting_machine_finger_guard` | grasp |
| `riveting_machine_rear_anchor` | `riveting_machine_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the spindle motor, riveting force, orbital tool path, stroke control or the two-hand safety logic.
