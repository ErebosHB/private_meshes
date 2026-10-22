# Mobile Shelving Run with Crank Drive

Three double-sided shelving units on floor rails: two carriages crank sideways to open an aisle next to the fixed unit.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per rail, carriage, upright, shelf and end panel, so every shelf and the aisle stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; hollow steel profiles as an equivalent 1,900; ABS/HDPE 1,050; particleboard 650 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `mobile_shelving_run_outer_carriage_joint` | prismatic | 0.75 |
| `mobile_shelving_run_outer_carriage_crank_joint` | continuous | 1.57 |
| `mobile_shelving_run_inner_carriage_joint` | prismatic | 0.75 |
| `mobile_shelving_run_inner_carriage_crank_joint` | continuous | 1.57 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `mobile_shelving_run_fixed_unit_shelf_surface` | `mobile_shelving_run_body` | place_surface |
| `mobile_shelving_run_wall_anchor` | `mobile_shelving_run_body` | wall_mount |
| `mobile_shelving_run_outer_carriage_shelf_surface` | `mobile_shelving_run_outer_carriage` | place_surface |
| `mobile_shelving_run_outer_carriage_crank_grip` | `mobile_shelving_run_outer_carriage_crank` | grasp |
| `mobile_shelving_run_inner_carriage_shelf_surface` | `mobile_shelving_run_inner_carriage` | place_surface |
| `mobile_shelving_run_inner_carriage_crank_grip` | `mobile_shelving_run_inner_carriage_crank` | grasp |

The URDF supplies geometry, articulation and frames. It does not model the crank gear ratio, carriage wheels on the rails, anti-tip guides, aisle locks or load ratings.
