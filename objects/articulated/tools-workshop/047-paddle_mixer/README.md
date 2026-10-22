# Paddle Mixer

Two-handled hand mixer standing on its helical paddle, with a trigger, lock button and speed dial.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, handle bar and paddle ring, so the space inside each handle loop and the paddle cage stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `paddle_mixer_spindle_joint` | continuous | 0.85 |
| `paddle_mixer_trigger_joint` | prismatic | 0.009 |
| `paddle_mixer_lock_button_joint` | prismatic | 0.004 |
| `paddle_mixer_speed_dial_joint` | revolute | 2.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `paddle_mixer_left_grip` | `paddle_mixer_body` | grasp |
| `paddle_mixer_right_grip` | `paddle_mixer_body` | grasp |
| `paddle_mixer_trigger_contact` | `paddle_mixer_trigger` | control |
| `paddle_mixer_lock_button_contact` | `paddle_mixer_lock_button` | control |
| `paddle_mixer_speed_dial_contact` | `paddle_mixer_speed_dial` | control |
| `paddle_mixer_paddle_head` | `paddle_mixer_spindle` | tool_attachment |
| `paddle_mixer_hanging_eye` | `paddle_mixer_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model motor torque, the gear stages, soft start, mixing loads, paddle wear or tip-over behaviour.
