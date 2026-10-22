# Welding Helmet

Flip-up welding helmet resting on its rim: the shell with its filter window pivots up on the headgear, which has a rear ratchet knob.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint, with the helmet resting on its lower rim.
Use a unique URDF parser prefix for each instance.
Collision uses one rounded box for the shell and cylinders around the headband, so the head space stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `welding_helmet_shell_joint` | revolute | 1.4 |
| `welding_helmet_ratchet_knob_joint` | revolute | 2.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `welding_helmet_shell_front_grip` | `welding_helmet_shell` | grasp |
| `welding_helmet_ratchet_knob_contact` | `welding_helmet_ratchet_knob` | control |
| `welding_helmet_head_space_volume` | `welding_helmet_headgear` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model the auto-darkening filter, sensors, pivot friction, headband sizing or padding.
