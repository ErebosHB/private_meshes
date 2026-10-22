# Angle Grinder

Compact 125 mm grinder lying disc-down, with a rotatable wheel guard, slide switch, spindle lock and side handle.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, guard segment, handle and the disc, so the gap between guard and disc stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `angle_grinder_guard_joint` | revolute | 1.15 |
| `angle_grinder_spindle_joint` | continuous | 0.7 |
| `angle_grinder_slide_switch_joint` | prismatic | 0.012 |
| `angle_grinder_spindle_lock_joint` | prismatic | 0.004 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `angle_grinder_body_grip` | `angle_grinder_body` | grasp |
| `angle_grinder_side_handle_grip` | `angle_grinder_body` | grasp |
| `angle_grinder_slide_switch_contact` | `angle_grinder_slide_switch` | control |
| `angle_grinder_spindle_lock_contact` | `angle_grinder_spindle_lock` | control |
| `angle_grinder_disc_face` | `angle_grinder_spindle` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model motor speed, kickback, restart protection, disc wear, sparks or the guard's clamping force.
