# Wall Cabinet, Wide, Lift-Up Flap

Low 1 m kitchen wall cabinet, 32 cm high, with a lift-up flap hinged along its top edge.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at the back-bottom edge centre.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so the compartment stays open behind the flap.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; particleboard 650 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wall_cabinet_wide_liftup_flap_flap_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wall_cabinet_wide_liftup_flap_flap_grip` | `wall_cabinet_wide_liftup_flap_flap` | grasp |
| `wall_cabinet_wide_liftup_flap_shelf_surface` | `wall_cabinet_wide_liftup_flap_body` | place_surface |
| `wall_cabinet_wide_liftup_flap_top_surface` | `wall_cabinet_wide_liftup_flap_body` | place_surface |
| `wall_cabinet_wide_liftup_flap_wall_anchor` | `wall_cabinet_wide_liftup_flap_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the flap stays, gas struts, load ratings, wall-fixing strength or assembly.
