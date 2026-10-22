# Tipping Skip on Castors

Steel tipping skip in a castor-mounted cradle with fork pockets; pulling the release lever lets the hopper roll forward and tip.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per hopper plate and cradle member and one cylinder per castor wheel, so the hopper stays open from above.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; hollow steel profiles as an equivalent 1,900; ABS/HDPE 1,050; rubber 1,200 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `tipping_skip_hopper_joint` | revolute | 0.9 |
| `tipping_skip_release_lever_joint` | revolute | 0.5 |
| `tipping_skip_front_left_castor_joint` | continuous | 0 |
| `tipping_skip_front_right_castor_joint` | continuous | 0 |
| `tipping_skip_rear_left_castor_joint` | continuous | 0 |
| `tipping_skip_rear_right_castor_joint` | continuous | 0 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `tipping_skip_fork_pocket_entry` | `tipping_skip_body` | tool_attachment |
| `tipping_skip_tether_anchor` | `tipping_skip_body` | wall_mount |
| `tipping_skip_hopper_back_grip` | `tipping_skip_hopper` | grasp |
| `tipping_skip_hopper_volume` | `tipping_skip_hopper` | container_volume |
| `tipping_skip_release_lever_knob` | `tipping_skip_release_lever` | control |

The URDF supplies geometry, articulation and frames. It does not model the rolling cradle curve, the self-righting balance, the latch spring, castor swivel, fork-lift handling or load ratings.
