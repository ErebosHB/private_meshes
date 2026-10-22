# Kids' Storage Frame with Bins

Low storage frame holding six pull-out bins in two columns.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so every bin stays open from above.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `kids_storage_frame_bins_left_bottom_bin_joint` | prismatic | 0.24 |
| `kids_storage_frame_bins_left_middle_bin_joint` | prismatic | 0.24 |
| `kids_storage_frame_bins_left_top_bin_joint` | prismatic | 0.24 |
| `kids_storage_frame_bins_right_bottom_bin_joint` | prismatic | 0.24 |
| `kids_storage_frame_bins_right_middle_bin_joint` | prismatic | 0.24 |
| `kids_storage_frame_bins_right_top_bin_joint` | prismatic | 0.24 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `kids_storage_frame_bins_left_bottom_bin_grip` | `kids_storage_frame_bins_left_bottom_bin` | grasp |
| `kids_storage_frame_bins_left_bottom_bin_volume` | `kids_storage_frame_bins_left_bottom_bin` | container_volume |
| `kids_storage_frame_bins_left_middle_bin_grip` | `kids_storage_frame_bins_left_middle_bin` | grasp |
| `kids_storage_frame_bins_left_middle_bin_volume` | `kids_storage_frame_bins_left_middle_bin` | container_volume |
| `kids_storage_frame_bins_left_top_bin_grip` | `kids_storage_frame_bins_left_top_bin` | grasp |
| `kids_storage_frame_bins_left_top_bin_volume` | `kids_storage_frame_bins_left_top_bin` | container_volume |
| `kids_storage_frame_bins_right_bottom_bin_grip` | `kids_storage_frame_bins_right_bottom_bin` | grasp |
| `kids_storage_frame_bins_right_bottom_bin_volume` | `kids_storage_frame_bins_right_bottom_bin` | container_volume |
| `kids_storage_frame_bins_right_middle_bin_grip` | `kids_storage_frame_bins_right_middle_bin` | grasp |
| `kids_storage_frame_bins_right_middle_bin_volume` | `kids_storage_frame_bins_right_middle_bin` | container_volume |
| `kids_storage_frame_bins_right_top_bin_grip` | `kids_storage_frame_bins_right_top_bin` | grasp |
| `kids_storage_frame_bins_right_top_bin_volume` | `kids_storage_frame_bins_right_top_bin` | container_volume |
| `kids_storage_frame_bins_top_surface` | `kids_storage_frame_bins_body` | place_surface |
| `kids_storage_frame_bins_wall_anchor` | `kids_storage_frame_bins_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model runner friction, load ratings, wall-fixing strength, assembly or tip-over behaviour.
