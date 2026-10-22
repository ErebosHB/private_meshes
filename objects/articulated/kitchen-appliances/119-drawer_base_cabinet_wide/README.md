# Wide Drawer Base Cabinet

1 m kitchen base cabinet with worktop and three drawers: a shallow cutlery drawer over two deep pan drawers.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per carcass panel, front and drawer-box wall, so the cupboard and every drawer stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; particleboard 650; pine 500 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `drawer_base_cabinet_wide_top_drawer_joint` | prismatic | 0.276 |
| `drawer_base_cabinet_wide_middle_drawer_joint` | prismatic | 0.276 |
| `drawer_base_cabinet_wide_bottom_drawer_joint` | prismatic | 0.276 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `drawer_base_cabinet_wide_top_drawer_grip` | `drawer_base_cabinet_wide_top_drawer` | grasp |
| `drawer_base_cabinet_wide_top_drawer_volume` | `drawer_base_cabinet_wide_top_drawer` | container_volume |
| `drawer_base_cabinet_wide_middle_drawer_grip` | `drawer_base_cabinet_wide_middle_drawer` | grasp |
| `drawer_base_cabinet_wide_middle_drawer_volume` | `drawer_base_cabinet_wide_middle_drawer` | container_volume |
| `drawer_base_cabinet_wide_bottom_drawer_grip` | `drawer_base_cabinet_wide_bottom_drawer` | grasp |
| `drawer_base_cabinet_wide_bottom_drawer_volume` | `drawer_base_cabinet_wide_bottom_drawer` | container_volume |
| `drawer_base_cabinet_wide_worktop_surface` | `drawer_base_cabinet_wide_body` | place_surface |
| `drawer_base_cabinet_wide_wall_anchor` | `drawer_base_cabinet_wide_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model hinge dampers, drawer runners, load ratings, wall-fixing strength, assembly or tip-over behaviour.
