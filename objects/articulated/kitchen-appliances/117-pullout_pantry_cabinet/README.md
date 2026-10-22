# Pull-Out Pantry Cabinet

Narrow full-height larder cabinet whose front pulls straight out on a single runner with five wire trays.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per carcass panel, tray floor and tray rail, so the trays stay open from the sides when pulled out.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; particleboard 650; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `pullout_pantry_cabinet_pullout_joint` | prismatic | 0.288 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `pullout_pantry_cabinet_pullout_grip` | `pullout_pantry_cabinet_pullout` | grasp |
| `pullout_pantry_cabinet_pullout_lower_tray_volume` | `pullout_pantry_cabinet_pullout` | container_volume |
| `pullout_pantry_cabinet_pullout_upper_tray_volume` | `pullout_pantry_cabinet_pullout` | container_volume |
| `pullout_pantry_cabinet_top_surface` | `pullout_pantry_cabinet_body` | place_surface |
| `pullout_pantry_cabinet_wall_anchor` | `pullout_pantry_cabinet_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the heavy-duty runner, soft-close, load ratings, wall-fixing strength, assembly or tip-over behaviour.
