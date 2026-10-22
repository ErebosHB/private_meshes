# Pallet Racking Bay with Pull-out Frames

Single bay of pallet racking with two beam levels; the lower level carries two pull-out pallet frames on rails.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per post, brace, beam, rail and frame member, so every pallet position stays open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; hollow steel profiles as an equivalent 1,900; ABS/HDPE 1,050 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `pallet_racking_bay_left_pullout_frame_joint` | prismatic | 0.6 |
| `pallet_racking_bay_right_pullout_frame_joint` | prismatic | 0.6 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `pallet_racking_bay_top_level_surface` | `pallet_racking_bay_body` | place_surface |
| `pallet_racking_bay_wall_anchor` | `pallet_racking_bay_body` | wall_mount |
| `pallet_racking_bay_left_pullout_frame_grip` | `pallet_racking_bay_left_pullout_frame` | grasp |
| `pallet_racking_bay_left_pullout_frame_surface` | `pallet_racking_bay_left_pullout_frame` | place_surface |
| `pallet_racking_bay_right_pullout_frame_grip` | `pallet_racking_bay_right_pullout_frame` | grasp |
| `pallet_racking_bay_right_pullout_frame_surface` | `pallet_racking_bay_right_pullout_frame` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model the rail bearings and end stops, beam safety locks, load ratings per level, anchor bolts or impact behaviour.
