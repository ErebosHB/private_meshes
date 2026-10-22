# Dual-Compartment Bin, Tall Narrow

Tall, narrow steel bin with a rear-hinged lid over two deep lift-out inner buckets.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing wall, lid plate and bucket wall, so the housing and both buckets stay open from above.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `dual_compartment_bin_tall_narrow_lid_joint` | revolute | 1.2 |
| `dual_compartment_bin_tall_narrow_left_bucket_joint` | prismatic | 0.137 |
| `dual_compartment_bin_tall_narrow_right_bucket_joint` | prismatic | 0.137 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `dual_compartment_bin_tall_narrow_lid_grip` | `dual_compartment_bin_tall_narrow_lid` | grasp |
| `dual_compartment_bin_tall_narrow_left_bucket_grip` | `dual_compartment_bin_tall_narrow_left_bucket` | grasp |
| `dual_compartment_bin_tall_narrow_left_bucket_volume` | `dual_compartment_bin_tall_narrow_left_bucket` | container_volume |
| `dual_compartment_bin_tall_narrow_right_bucket_grip` | `dual_compartment_bin_tall_narrow_right_bucket` | grasp |
| `dual_compartment_bin_tall_narrow_right_bucket_volume` | `dual_compartment_bin_tall_narrow_right_bucket` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model the lid damper, a pedal or sensor opening, odour filters, bag clamps or load ratings.
