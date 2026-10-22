# Kitchen Run, Cabinets Only, Long

3.3 m cabinet run with a tall fridge housing, wide drawers, double sink, an open dishwasher niche and an oven housing.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per carcass panel, front, worktop piece and appliance wall, so every cupboard, drawer, niche, basin and appliance cavity stays open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; particleboard 650; pine 500; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `kitchen_run_cabinets_long_b1_bottom_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_long_b1_top_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_long_b2_top_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_cabinets_long_b2_middle_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_cabinets_long_b2_bottom_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_cabinets_long_sink_left_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_long_sink_right_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_long_b5_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_cabinets_long_w2_flap_joint` | revolute | 1.2 |
| `kitchen_run_cabinets_long_w3_left_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_long_w3_right_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_long_w4_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_long_w5_flap_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `kitchen_run_cabinets_long_b1_bottom_door_grip` | `kitchen_run_cabinets_long_b1_bottom_door` | grasp |
| `kitchen_run_cabinets_long_b1_top_door_grip` | `kitchen_run_cabinets_long_b1_top_door` | grasp |
| `kitchen_run_cabinets_long_b1_appliance_niche_volume` | `kitchen_run_cabinets_long_body` | container_volume |
| `kitchen_run_cabinets_long_b2_top_drawer_grip` | `kitchen_run_cabinets_long_b2_top_drawer` | grasp |
| `kitchen_run_cabinets_long_b2_top_drawer_volume` | `kitchen_run_cabinets_long_b2_top_drawer` | container_volume |
| `kitchen_run_cabinets_long_b2_middle_drawer_grip` | `kitchen_run_cabinets_long_b2_middle_drawer` | grasp |
| `kitchen_run_cabinets_long_b2_middle_drawer_volume` | `kitchen_run_cabinets_long_b2_middle_drawer` | container_volume |
| `kitchen_run_cabinets_long_b2_bottom_drawer_grip` | `kitchen_run_cabinets_long_b2_bottom_drawer` | grasp |
| `kitchen_run_cabinets_long_b2_bottom_drawer_volume` | `kitchen_run_cabinets_long_b2_bottom_drawer` | container_volume |
| `kitchen_run_cabinets_long_sink_left_door_grip` | `kitchen_run_cabinets_long_sink_left_door` | grasp |
| `kitchen_run_cabinets_long_sink_right_door_grip` | `kitchen_run_cabinets_long_sink_right_door` | grasp |
| `kitchen_run_cabinets_long_sink_basin_volume` | `kitchen_run_cabinets_long_body` | container_volume |
| `kitchen_run_cabinets_long_b4_appliance_niche_volume` | `kitchen_run_cabinets_long_body` | container_volume |
| `kitchen_run_cabinets_long_b5_drawer_grip` | `kitchen_run_cabinets_long_b5_drawer` | grasp |
| `kitchen_run_cabinets_long_b5_drawer_volume` | `kitchen_run_cabinets_long_b5_drawer` | container_volume |
| `kitchen_run_cabinets_long_b5_oven_niche_volume` | `kitchen_run_cabinets_long_body` | container_volume |
| `kitchen_run_cabinets_long_w2_flap_grip` | `kitchen_run_cabinets_long_w2_flap` | grasp |
| `kitchen_run_cabinets_long_w3_left_door_grip` | `kitchen_run_cabinets_long_w3_left_door` | grasp |
| `kitchen_run_cabinets_long_w3_right_door_grip` | `kitchen_run_cabinets_long_w3_right_door` | grasp |
| `kitchen_run_cabinets_long_w4_door_grip` | `kitchen_run_cabinets_long_w4_door` | grasp |
| `kitchen_run_cabinets_long_w5_flap_grip` | `kitchen_run_cabinets_long_w5_flap` | grasp |
| `kitchen_run_cabinets_long_w5_hood_niche_volume` | `kitchen_run_cabinets_long_body` | container_volume |
| `kitchen_run_cabinets_long_worktop_surface` | `kitchen_run_cabinets_long_body` | place_surface |
| `kitchen_run_cabinets_long_wall_anchor` | `kitchen_run_cabinets_long_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model appliance installation, water connection, hinge dampers, drawer runners, load ratings, wall-fixing strength or assembly.
