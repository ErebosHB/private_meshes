# Kitchen Run with Appliances, Long

3.3 m kitchen with a tall fridge-freezer housing, drawers, double sink, dishwasher, oven with hob and a narrow pull-out.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per carcass panel, front, worktop piece and appliance wall, so every cupboard, drawer, niche, basin and appliance cavity stays open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; aluminium 2,700; glass 2,500; particleboard 650; pine 500; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `kitchen_run_appliances_long_freezer_door_joint` | revolute | 1.4 |
| `kitchen_run_appliances_long_fridge_door_joint` | revolute | 1.4 |
| `kitchen_run_appliances_long_b1_top_door_joint` | revolute | 1.4 |
| `kitchen_run_appliances_long_freezer_drawer_1_joint` | prismatic | 0.252 |
| `kitchen_run_appliances_long_freezer_drawer_2_joint` | prismatic | 0.252 |
| `kitchen_run_appliances_long_b2_top_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_appliances_long_b2_middle_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_appliances_long_b2_bottom_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_appliances_long_sink_left_door_joint` | revolute | 1.4 |
| `kitchen_run_appliances_long_sink_right_door_joint` | revolute | 1.4 |
| `kitchen_run_appliances_long_dishwasher_door_joint` | revolute | 1.5 |
| `kitchen_run_appliances_long_dishwasher_lower_rack_joint` | prismatic | 0.288 |
| `kitchen_run_appliances_long_dishwasher_upper_rack_joint` | prismatic | 0.288 |
| `kitchen_run_appliances_long_oven_storage_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_appliances_long_oven_knob_1_joint` | revolute | 1.57 |
| `kitchen_run_appliances_long_oven_knob_2_joint` | revolute | 1.57 |
| `kitchen_run_appliances_long_oven_door_joint` | revolute | 1.2 |
| `kitchen_run_appliances_long_b6_pullout_joint` | prismatic | 0.276 |
| `kitchen_run_appliances_long_w2_flap_joint` | revolute | 1.2 |
| `kitchen_run_appliances_long_w3_left_door_joint` | revolute | 1.4 |
| `kitchen_run_appliances_long_w3_right_door_joint` | revolute | 1.4 |
| `kitchen_run_appliances_long_w4_door_joint` | revolute | 1.4 |
| `kitchen_run_appliances_long_hood_visor_joint` | prismatic | 0.16 |
| `kitchen_run_appliances_long_w5_flap_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `kitchen_run_appliances_long_freezer_door_grip` | `kitchen_run_appliances_long_freezer_door` | grasp |
| `kitchen_run_appliances_long_fridge_door_grip` | `kitchen_run_appliances_long_fridge_door` | grasp |
| `kitchen_run_appliances_long_b1_top_door_grip` | `kitchen_run_appliances_long_b1_top_door` | grasp |
| `kitchen_run_appliances_long_freezer_drawer_1_volume` | `kitchen_run_appliances_long_freezer_drawer_1` | container_volume |
| `kitchen_run_appliances_long_freezer_drawer_1_grip` | `kitchen_run_appliances_long_freezer_drawer_1` | grasp |
| `kitchen_run_appliances_long_freezer_drawer_2_volume` | `kitchen_run_appliances_long_freezer_drawer_2` | container_volume |
| `kitchen_run_appliances_long_freezer_drawer_2_grip` | `kitchen_run_appliances_long_freezer_drawer_2` | grasp |
| `kitchen_run_appliances_long_fridge_volume` | `kitchen_run_appliances_long_body` | container_volume |
| `kitchen_run_appliances_long_b2_top_drawer_grip` | `kitchen_run_appliances_long_b2_top_drawer` | grasp |
| `kitchen_run_appliances_long_b2_top_drawer_volume` | `kitchen_run_appliances_long_b2_top_drawer` | container_volume |
| `kitchen_run_appliances_long_b2_middle_drawer_grip` | `kitchen_run_appliances_long_b2_middle_drawer` | grasp |
| `kitchen_run_appliances_long_b2_middle_drawer_volume` | `kitchen_run_appliances_long_b2_middle_drawer` | container_volume |
| `kitchen_run_appliances_long_b2_bottom_drawer_grip` | `kitchen_run_appliances_long_b2_bottom_drawer` | grasp |
| `kitchen_run_appliances_long_b2_bottom_drawer_volume` | `kitchen_run_appliances_long_b2_bottom_drawer` | container_volume |
| `kitchen_run_appliances_long_sink_left_door_grip` | `kitchen_run_appliances_long_sink_left_door` | grasp |
| `kitchen_run_appliances_long_sink_right_door_grip` | `kitchen_run_appliances_long_sink_right_door` | grasp |
| `kitchen_run_appliances_long_sink_basin_volume` | `kitchen_run_appliances_long_body` | container_volume |
| `kitchen_run_appliances_long_dishwasher_tub_volume` | `kitchen_run_appliances_long_body` | container_volume |
| `kitchen_run_appliances_long_dishwasher_door_grip` | `kitchen_run_appliances_long_dishwasher_door` | grasp |
| `kitchen_run_appliances_long_dishwasher_lower_rack_grip` | `kitchen_run_appliances_long_dishwasher_lower_rack` | grasp |
| `kitchen_run_appliances_long_dishwasher_lower_rack_volume` | `kitchen_run_appliances_long_dishwasher_lower_rack` | container_volume |
| `kitchen_run_appliances_long_dishwasher_upper_rack_grip` | `kitchen_run_appliances_long_dishwasher_upper_rack` | grasp |
| `kitchen_run_appliances_long_dishwasher_upper_rack_volume` | `kitchen_run_appliances_long_dishwasher_upper_rack` | container_volume |
| `kitchen_run_appliances_long_oven_storage_drawer_grip` | `kitchen_run_appliances_long_oven_storage_drawer` | grasp |
| `kitchen_run_appliances_long_oven_storage_drawer_volume` | `kitchen_run_appliances_long_oven_storage_drawer` | container_volume |
| `kitchen_run_appliances_long_oven_cavity_volume` | `kitchen_run_appliances_long_body` | container_volume |
| `kitchen_run_appliances_long_oven_knob_1_contact` | `kitchen_run_appliances_long_oven_knob_1` | control |
| `kitchen_run_appliances_long_oven_knob_2_contact` | `kitchen_run_appliances_long_oven_knob_2` | control |
| `kitchen_run_appliances_long_oven_door_grip` | `kitchen_run_appliances_long_oven_door` | grasp |
| `kitchen_run_appliances_long_hob_surface` | `kitchen_run_appliances_long_body` | place_surface |
| `kitchen_run_appliances_long_b6_pullout_grip` | `kitchen_run_appliances_long_b6_pullout` | grasp |
| `kitchen_run_appliances_long_b6_pullout_volume` | `kitchen_run_appliances_long_b6_pullout` | container_volume |
| `kitchen_run_appliances_long_w2_flap_grip` | `kitchen_run_appliances_long_w2_flap` | grasp |
| `kitchen_run_appliances_long_w3_left_door_grip` | `kitchen_run_appliances_long_w3_left_door` | grasp |
| `kitchen_run_appliances_long_w3_right_door_grip` | `kitchen_run_appliances_long_w3_right_door` | grasp |
| `kitchen_run_appliances_long_w4_door_grip` | `kitchen_run_appliances_long_w4_door` | grasp |
| `kitchen_run_appliances_long_hood_visor_grip` | `kitchen_run_appliances_long_hood_visor` | grasp |
| `kitchen_run_appliances_long_w5_flap_grip` | `kitchen_run_appliances_long_w5_flap` | grasp |
| `kitchen_run_appliances_long_w6_shelf_surface` | `kitchen_run_appliances_long_body` | place_surface |
| `kitchen_run_appliances_long_worktop_surface` | `kitchen_run_appliances_long_body` | place_surface |
| `kitchen_run_appliances_long_wall_anchor` | `kitchen_run_appliances_long_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model cooking heat, refrigeration, water supply and drainage, dishwasher cycles, hinge dampers, drawer runners, load ratings, wall-fixing strength or assembly.
