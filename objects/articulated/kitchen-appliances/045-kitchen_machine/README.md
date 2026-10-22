# Tilt-Head Kitchen Machine

Stand mixer with a tilting motor head carrying a beater, a mixing bowl on the base and a speed dial.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes for the base, column, head and beater, and twelve wall segments plus a floor disc for the bowl, so the bowl stays open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; aluminium 2,700; enamelled steel 7,850; rubber 1,100; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `kitchen_machine_speed_dial_joint` | revolute | 1.57 |
| `kitchen_machine_head_joint` | revolute | 0.55 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `kitchen_machine_speed_dial_contact` | `kitchen_machine_speed_dial` | control |
| `kitchen_machine_head_grip` | `kitchen_machine_head` | grasp |
| `kitchen_machine_beater_attachment` | `kitchen_machine_head` | tool_attachment |
| `kitchen_machine_bowl_volume` | `kitchen_machine_body` | container_volume |
| `kitchen_machine_carry_grip` | `kitchen_machine_body` | grasp |

The URDF supplies geometry, articulation and frames. It does not model the motor, planetary beater action, the head lock, dough loads or bowl clamping.
