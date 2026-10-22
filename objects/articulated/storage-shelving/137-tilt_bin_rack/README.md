# Tilt Bin Rack

Steel rack of nine tilt-out bins in three rows; each bin pivots at its front lower edge to present its contents.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per frame panel, shelf, divider and bin wall, so every bin stays open from above.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; ABS/HDPE 1,050 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `tilt_bin_rack_bin_r1c1_joint` | revolute | 0.35 |
| `tilt_bin_rack_bin_r1c2_joint` | revolute | 0.35 |
| `tilt_bin_rack_bin_r1c3_joint` | revolute | 0.35 |
| `tilt_bin_rack_bin_r2c1_joint` | revolute | 0.35 |
| `tilt_bin_rack_bin_r2c2_joint` | revolute | 0.35 |
| `tilt_bin_rack_bin_r2c3_joint` | revolute | 0.35 |
| `tilt_bin_rack_bin_r3c1_joint` | revolute | 0.35 |
| `tilt_bin_rack_bin_r3c2_joint` | revolute | 0.35 |
| `tilt_bin_rack_bin_r3c3_joint` | revolute | 0.35 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `tilt_bin_rack_top_surface` | `tilt_bin_rack_body` | place_surface |
| `tilt_bin_rack_bin_r1c1_grip` | `tilt_bin_rack_bin_r1c1` | grasp |
| `tilt_bin_rack_bin_r1c1_volume` | `tilt_bin_rack_bin_r1c1` | container_volume |
| `tilt_bin_rack_bin_r1c2_grip` | `tilt_bin_rack_bin_r1c2` | grasp |
| `tilt_bin_rack_bin_r1c2_volume` | `tilt_bin_rack_bin_r1c2` | container_volume |
| `tilt_bin_rack_bin_r1c3_grip` | `tilt_bin_rack_bin_r1c3` | grasp |
| `tilt_bin_rack_bin_r1c3_volume` | `tilt_bin_rack_bin_r1c3` | container_volume |
| `tilt_bin_rack_bin_r2c1_grip` | `tilt_bin_rack_bin_r2c1` | grasp |
| `tilt_bin_rack_bin_r2c1_volume` | `tilt_bin_rack_bin_r2c1` | container_volume |
| `tilt_bin_rack_bin_r2c2_grip` | `tilt_bin_rack_bin_r2c2` | grasp |
| `tilt_bin_rack_bin_r2c2_volume` | `tilt_bin_rack_bin_r2c2` | container_volume |
| `tilt_bin_rack_bin_r2c3_grip` | `tilt_bin_rack_bin_r2c3` | grasp |
| `tilt_bin_rack_bin_r2c3_volume` | `tilt_bin_rack_bin_r2c3` | container_volume |
| `tilt_bin_rack_bin_r3c1_grip` | `tilt_bin_rack_bin_r3c1` | grasp |
| `tilt_bin_rack_bin_r3c1_volume` | `tilt_bin_rack_bin_r3c1` | container_volume |
| `tilt_bin_rack_bin_r3c2_grip` | `tilt_bin_rack_bin_r3c2` | grasp |
| `tilt_bin_rack_bin_r3c2_volume` | `tilt_bin_rack_bin_r3c2` | container_volume |
| `tilt_bin_rack_bin_r3c3_grip` | `tilt_bin_rack_bin_r3c3` | grasp |
| `tilt_bin_rack_bin_r3c3_volume` | `tilt_bin_rack_bin_r3c3` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model the bin stops and detents, label holders, bench or wall fixing, or load ratings per bin.
