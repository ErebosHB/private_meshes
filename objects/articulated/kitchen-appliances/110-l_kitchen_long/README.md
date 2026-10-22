# L-Shaped Kitchen, Long

Corner kitchen, 3.7 m by 1.72 m, ending in a tall fridge-freezer housing, with double sink, dishwasher and a pull-out along the wall and oven with hob on the return.

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
| `l_kitchen_long_b1_corner_door_joint` | revolute | 1.4 |
| `l_kitchen_long_b1_corner_basket_joint` | prismatic | 0.264 |
| `l_kitchen_long_b2_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_long_b2_door_joint` | revolute | 1.4 |
| `l_kitchen_long_sink_left_door_joint` | revolute | 1.4 |
| `l_kitchen_long_sink_right_door_joint` | revolute | 1.4 |
| `l_kitchen_long_dishwasher_door_joint` | revolute | 1.5 |
| `l_kitchen_long_dishwasher_lower_rack_joint` | prismatic | 0.288 |
| `l_kitchen_long_dishwasher_upper_rack_joint` | prismatic | 0.288 |
| `l_kitchen_long_b5_pullout_joint` | prismatic | 0.276 |
| `l_kitchen_long_freezer_door_joint` | revolute | 1.4 |
| `l_kitchen_long_fridge_door_joint` | revolute | 1.4 |
| `l_kitchen_long_b6_top_door_joint` | revolute | 1.4 |
| `l_kitchen_long_freezer_drawer_1_joint` | prismatic | 0.252 |
| `l_kitchen_long_freezer_drawer_2_joint` | prismatic | 0.252 |
| `l_kitchen_long_w1_left_door_joint` | revolute | 1.4 |
| `l_kitchen_long_w1_right_door_joint` | revolute | 1.4 |
| `l_kitchen_long_w2_flap_joint` | revolute | 1.2 |
| `l_kitchen_long_w3_left_door_joint` | revolute | 1.4 |
| `l_kitchen_long_w3_right_door_joint` | revolute | 1.4 |
| `l_kitchen_long_w4_door_joint` | revolute | 1.4 |
| `l_kitchen_long_oven_storage_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_long_oven_knob_1_joint` | revolute | 1.57 |
| `l_kitchen_long_oven_knob_2_joint` | revolute | 1.57 |
| `l_kitchen_long_oven_door_joint` | revolute | 1.2 |
| `l_kitchen_long_rb2_top_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_long_rb2_middle_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_long_rb2_bottom_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_long_hood_visor_joint` | prismatic | 0.16 |
| `l_kitchen_long_rw1_flap_joint` | revolute | 1.2 |
| `l_kitchen_long_rw2_flap_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `l_kitchen_long_b1_corner_door_grip` | `l_kitchen_long_b1_corner_door` | grasp |
| `l_kitchen_long_b1_corner_basket_volume` | `l_kitchen_long_b1_corner_basket` | container_volume |
| `l_kitchen_long_b1_corner_basket_grip` | `l_kitchen_long_b1_corner_basket` | grasp |
| `l_kitchen_long_b2_drawer_grip` | `l_kitchen_long_b2_drawer` | grasp |
| `l_kitchen_long_b2_drawer_volume` | `l_kitchen_long_b2_drawer` | container_volume |
| `l_kitchen_long_b2_door_grip` | `l_kitchen_long_b2_door` | grasp |
| `l_kitchen_long_sink_left_door_grip` | `l_kitchen_long_sink_left_door` | grasp |
| `l_kitchen_long_sink_right_door_grip` | `l_kitchen_long_sink_right_door` | grasp |
| `l_kitchen_long_sink_basin_volume` | `l_kitchen_long_body` | container_volume |
| `l_kitchen_long_dishwasher_tub_volume` | `l_kitchen_long_body` | container_volume |
| `l_kitchen_long_dishwasher_door_grip` | `l_kitchen_long_dishwasher_door` | grasp |
| `l_kitchen_long_dishwasher_lower_rack_grip` | `l_kitchen_long_dishwasher_lower_rack` | grasp |
| `l_kitchen_long_dishwasher_lower_rack_volume` | `l_kitchen_long_dishwasher_lower_rack` | container_volume |
| `l_kitchen_long_dishwasher_upper_rack_grip` | `l_kitchen_long_dishwasher_upper_rack` | grasp |
| `l_kitchen_long_dishwasher_upper_rack_volume` | `l_kitchen_long_dishwasher_upper_rack` | container_volume |
| `l_kitchen_long_b5_pullout_grip` | `l_kitchen_long_b5_pullout` | grasp |
| `l_kitchen_long_b5_pullout_volume` | `l_kitchen_long_b5_pullout` | container_volume |
| `l_kitchen_long_freezer_door_grip` | `l_kitchen_long_freezer_door` | grasp |
| `l_kitchen_long_fridge_door_grip` | `l_kitchen_long_fridge_door` | grasp |
| `l_kitchen_long_b6_top_door_grip` | `l_kitchen_long_b6_top_door` | grasp |
| `l_kitchen_long_freezer_drawer_1_volume` | `l_kitchen_long_freezer_drawer_1` | container_volume |
| `l_kitchen_long_freezer_drawer_1_grip` | `l_kitchen_long_freezer_drawer_1` | grasp |
| `l_kitchen_long_freezer_drawer_2_volume` | `l_kitchen_long_freezer_drawer_2` | container_volume |
| `l_kitchen_long_freezer_drawer_2_grip` | `l_kitchen_long_freezer_drawer_2` | grasp |
| `l_kitchen_long_fridge_volume` | `l_kitchen_long_body` | container_volume |
| `l_kitchen_long_w1_left_door_grip` | `l_kitchen_long_w1_left_door` | grasp |
| `l_kitchen_long_w1_right_door_grip` | `l_kitchen_long_w1_right_door` | grasp |
| `l_kitchen_long_w2_flap_grip` | `l_kitchen_long_w2_flap` | grasp |
| `l_kitchen_long_w3_left_door_grip` | `l_kitchen_long_w3_left_door` | grasp |
| `l_kitchen_long_w3_right_door_grip` | `l_kitchen_long_w3_right_door` | grasp |
| `l_kitchen_long_w4_door_grip` | `l_kitchen_long_w4_door` | grasp |
| `l_kitchen_long_w5_shelf_surface` | `l_kitchen_long_body` | place_surface |
| `l_kitchen_long_oven_storage_drawer_grip` | `l_kitchen_long_oven_storage_drawer` | grasp |
| `l_kitchen_long_oven_storage_drawer_volume` | `l_kitchen_long_oven_storage_drawer` | container_volume |
| `l_kitchen_long_oven_cavity_volume` | `l_kitchen_long_body` | container_volume |
| `l_kitchen_long_oven_knob_1_contact` | `l_kitchen_long_oven_knob_1` | control |
| `l_kitchen_long_oven_knob_2_contact` | `l_kitchen_long_oven_knob_2` | control |
| `l_kitchen_long_oven_door_grip` | `l_kitchen_long_oven_door` | grasp |
| `l_kitchen_long_hob_surface` | `l_kitchen_long_body` | place_surface |
| `l_kitchen_long_rb2_top_drawer_grip` | `l_kitchen_long_rb2_top_drawer` | grasp |
| `l_kitchen_long_rb2_top_drawer_volume` | `l_kitchen_long_rb2_top_drawer` | container_volume |
| `l_kitchen_long_rb2_middle_drawer_grip` | `l_kitchen_long_rb2_middle_drawer` | grasp |
| `l_kitchen_long_rb2_middle_drawer_volume` | `l_kitchen_long_rb2_middle_drawer` | container_volume |
| `l_kitchen_long_rb2_bottom_drawer_grip` | `l_kitchen_long_rb2_bottom_drawer` | grasp |
| `l_kitchen_long_rb2_bottom_drawer_volume` | `l_kitchen_long_rb2_bottom_drawer` | container_volume |
| `l_kitchen_long_hood_visor_grip` | `l_kitchen_long_hood_visor` | grasp |
| `l_kitchen_long_rw1_flap_grip` | `l_kitchen_long_rw1_flap` | grasp |
| `l_kitchen_long_rw2_flap_grip` | `l_kitchen_long_rw2_flap` | grasp |
| `l_kitchen_long_worktop_surface` | `l_kitchen_long_body` | place_surface |
| `l_kitchen_long_return_worktop_surface` | `l_kitchen_long_body` | place_surface |
| `l_kitchen_long_wall_anchor` | `l_kitchen_long_body` | wall_mount |
| `l_kitchen_long_return_wall_anchor` | `l_kitchen_long_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model cooking heat, refrigeration, water supply and drainage, dishwasher cycles, hinge dampers, drawer runners, load ratings, wall-fixing strength or assembly.
