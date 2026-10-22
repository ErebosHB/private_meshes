# Rotary Hammer

Pistol-grip hammer drill with a swivelling side handle, sliding depth rod, mode selector and trigger.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, handle and the bit, so the opening between motor block and rear grip stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `rotary_hammer_side_handle_joint` | revolute | 1.3 |
| `rotary_hammer_depth_rod_joint` | prismatic | 0.09 |
| `rotary_hammer_mode_selector_joint` | revolute | 1.57 |
| `rotary_hammer_trigger_joint` | prismatic | 0.008 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `rotary_hammer_rear_grip` | `rotary_hammer_body` | grasp |
| `rotary_hammer_side_handle_grip` | `rotary_hammer_side_handle` | grasp |
| `rotary_hammer_trigger_contact` | `rotary_hammer_trigger` | control |
| `rotary_hammer_mode_selector_contact` | `rotary_hammer_mode_selector` | control |
| `rotary_hammer_bit_tip` | `rotary_hammer_body` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the hammer mechanism, impact energy, the slip clutch, vibration damping, bit retention or dust.
