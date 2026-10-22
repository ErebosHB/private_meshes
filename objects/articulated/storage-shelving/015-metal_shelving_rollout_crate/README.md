# Metal Utility Shelving with Roll-out Crate

Steel utility shelving with four shelf levels and a roll-out crate on casters below.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so every shelf level and the crate stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `metal_shelving_rollout_crate_crate_joint` | prismatic | 0.20 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `metal_shelving_rollout_crate_crate_grip` | `metal_shelving_rollout_crate_crate` | grasp |
| `metal_shelving_rollout_crate_crate_volume` | `metal_shelving_rollout_crate_crate` | container_volume |
| `metal_shelving_rollout_crate_lower_shelf_surface` | `metal_shelving_rollout_crate_body` | place_surface |
| `metal_shelving_rollout_crate_middle_shelf_surface` | `metal_shelving_rollout_crate_body` | place_surface |
| `metal_shelving_rollout_crate_upper_shelf_surface` | `metal_shelving_rollout_crate_body` | place_surface |
| `metal_shelving_rollout_crate_top_surface` | `metal_shelving_rollout_crate_body` | place_surface |
| `metal_shelving_rollout_crate_wall_anchor` | `metal_shelving_rollout_crate_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model caster rolling, shelf deflection, load ratings, wall-fixing strength, assembly or tip-over behaviour.
