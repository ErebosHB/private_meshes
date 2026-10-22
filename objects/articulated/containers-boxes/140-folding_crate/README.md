# Folding Crate

Plastic crate whose four walls hinge at the base and fold flat: long walls first, short walls on top.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per base panel, rim and wall, so the crate stays open from above when erected.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS/HDPE 1,050 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `folding_crate_front_wall_joint` | revolute | 1.57 |
| `folding_crate_back_wall_joint` | revolute | 1.57 |
| `folding_crate_left_wall_joint` | revolute | 1.57 |
| `folding_crate_right_wall_joint` | revolute | 1.57 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `folding_crate_crate_volume` | `folding_crate_body` | container_volume |
| `folding_crate_left_wall_grip` | `folding_crate_left_wall` | grasp |
| `folding_crate_right_wall_grip` | `folding_crate_right_wall` | grasp |

The URDF supplies geometry, articulation and frames. It does not model the wall latches and their release order, stacking loads, lid accessories or load ratings.
