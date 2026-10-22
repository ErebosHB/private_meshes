# Small-Parts Cabinet with Clear Drawers

Bench or wall cabinet with twelve clear drawers in a three-by-four grid, each pulling out on its own runners.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing panel, divider and drawer wall, so every drawer compartment stays open from above.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS/HDPE 1,050; polycarbonate 1,200 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `small_parts_cabinet_drawer_r4c1_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r4c2_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r4c3_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r3c1_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r3c2_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r3c3_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r2c1_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r2c2_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r2c3_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r1c1_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r1c2_joint` | prismatic | 0.114 |
| `small_parts_cabinet_drawer_r1c3_joint` | prismatic | 0.114 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `small_parts_cabinet_top_surface` | `small_parts_cabinet_body` | place_surface |
| `small_parts_cabinet_drawer_r4c1_grip` | `small_parts_cabinet_drawer_r4c1` | grasp |
| `small_parts_cabinet_drawer_r4c1_volume` | `small_parts_cabinet_drawer_r4c1` | container_volume |
| `small_parts_cabinet_drawer_r4c2_grip` | `small_parts_cabinet_drawer_r4c2` | grasp |
| `small_parts_cabinet_drawer_r4c2_volume` | `small_parts_cabinet_drawer_r4c2` | container_volume |
| `small_parts_cabinet_drawer_r4c3_grip` | `small_parts_cabinet_drawer_r4c3` | grasp |
| `small_parts_cabinet_drawer_r4c3_volume` | `small_parts_cabinet_drawer_r4c3` | container_volume |
| `small_parts_cabinet_drawer_r3c1_grip` | `small_parts_cabinet_drawer_r3c1` | grasp |
| `small_parts_cabinet_drawer_r3c1_volume` | `small_parts_cabinet_drawer_r3c1` | container_volume |
| `small_parts_cabinet_drawer_r3c2_grip` | `small_parts_cabinet_drawer_r3c2` | grasp |
| `small_parts_cabinet_drawer_r3c2_volume` | `small_parts_cabinet_drawer_r3c2` | container_volume |
| `small_parts_cabinet_drawer_r3c3_grip` | `small_parts_cabinet_drawer_r3c3` | grasp |
| `small_parts_cabinet_drawer_r3c3_volume` | `small_parts_cabinet_drawer_r3c3` | container_volume |
| `small_parts_cabinet_drawer_r2c1_grip` | `small_parts_cabinet_drawer_r2c1` | grasp |
| `small_parts_cabinet_drawer_r2c1_volume` | `small_parts_cabinet_drawer_r2c1` | container_volume |
| `small_parts_cabinet_drawer_r2c2_grip` | `small_parts_cabinet_drawer_r2c2` | grasp |
| `small_parts_cabinet_drawer_r2c2_volume` | `small_parts_cabinet_drawer_r2c2` | container_volume |
| `small_parts_cabinet_drawer_r2c3_grip` | `small_parts_cabinet_drawer_r2c3` | grasp |
| `small_parts_cabinet_drawer_r2c3_volume` | `small_parts_cabinet_drawer_r2c3` | container_volume |
| `small_parts_cabinet_drawer_r1c1_grip` | `small_parts_cabinet_drawer_r1c1` | grasp |
| `small_parts_cabinet_drawer_r1c1_volume` | `small_parts_cabinet_drawer_r1c1` | container_volume |
| `small_parts_cabinet_drawer_r1c2_grip` | `small_parts_cabinet_drawer_r1c2` | grasp |
| `small_parts_cabinet_drawer_r1c2_volume` | `small_parts_cabinet_drawer_r1c2` | container_volume |
| `small_parts_cabinet_drawer_r1c3_grip` | `small_parts_cabinet_drawer_r1c3` | grasp |
| `small_parts_cabinet_drawer_r1c3_volume` | `small_parts_cabinet_drawer_r1c3` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model drawer stops, dividers inside the drawers, label inserts, wall-hanging keyholes or load ratings.
