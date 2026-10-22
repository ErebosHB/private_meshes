# L-Shaped Kitchen, Two Long Legs

Corner kitchen, 2.6 m by 2.8 m, with sink and dishwasher along the wall and a tall fridge-freezer, oven with hob and drawers along the long return.

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
| `l_kitchen_two_long_legs_b1_corner_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_b1_corner_basket_joint` | prismatic | 0.264 |
| `l_kitchen_two_long_legs_sink_left_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_sink_right_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_dishwasher_door_joint` | revolute | 1.5 |
| `l_kitchen_two_long_legs_dishwasher_lower_rack_joint` | prismatic | 0.288 |
| `l_kitchen_two_long_legs_dishwasher_upper_rack_joint` | prismatic | 0.288 |
| `l_kitchen_two_long_legs_b4_pullout_joint` | prismatic | 0.276 |
| `l_kitchen_two_long_legs_w1_left_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_w1_right_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_w2_left_glass_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_w2_right_glass_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_w3_glass_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_freezer_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_fridge_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_rb1_top_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_freezer_drawer_1_joint` | prismatic | 0.252 |
| `l_kitchen_two_long_legs_freezer_drawer_2_joint` | prismatic | 0.252 |
| `l_kitchen_two_long_legs_rb2_door_joint` | revolute | 1.4 |
| `l_kitchen_two_long_legs_oven_storage_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_two_long_legs_oven_knob_1_joint` | revolute | 1.57 |
| `l_kitchen_two_long_legs_oven_knob_2_joint` | revolute | 1.57 |
| `l_kitchen_two_long_legs_oven_door_joint` | revolute | 1.2 |
| `l_kitchen_two_long_legs_rb4_top_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_two_long_legs_rb4_middle_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_two_long_legs_rb4_bottom_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_two_long_legs_rw2_flap_joint` | revolute | 1.2 |
| `l_kitchen_two_long_legs_hood_visor_joint` | prismatic | 0.16 |
| `l_kitchen_two_long_legs_rw3_flap_joint` | revolute | 1.2 |
| `l_kitchen_two_long_legs_rw4_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `l_kitchen_two_long_legs_b1_corner_door_grip` | `l_kitchen_two_long_legs_b1_corner_door` | grasp |
| `l_kitchen_two_long_legs_b1_corner_basket_volume` | `l_kitchen_two_long_legs_b1_corner_basket` | container_volume |
| `l_kitchen_two_long_legs_b1_corner_basket_grip` | `l_kitchen_two_long_legs_b1_corner_basket` | grasp |
| `l_kitchen_two_long_legs_sink_left_door_grip` | `l_kitchen_two_long_legs_sink_left_door` | grasp |
| `l_kitchen_two_long_legs_sink_right_door_grip` | `l_kitchen_two_long_legs_sink_right_door` | grasp |
| `l_kitchen_two_long_legs_sink_basin_volume` | `l_kitchen_two_long_legs_body` | container_volume |
| `l_kitchen_two_long_legs_dishwasher_tub_volume` | `l_kitchen_two_long_legs_body` | container_volume |
| `l_kitchen_two_long_legs_dishwasher_door_grip` | `l_kitchen_two_long_legs_dishwasher_door` | grasp |
| `l_kitchen_two_long_legs_dishwasher_lower_rack_grip` | `l_kitchen_two_long_legs_dishwasher_lower_rack` | grasp |
| `l_kitchen_two_long_legs_dishwasher_lower_rack_volume` | `l_kitchen_two_long_legs_dishwasher_lower_rack` | container_volume |
| `l_kitchen_two_long_legs_dishwasher_upper_rack_grip` | `l_kitchen_two_long_legs_dishwasher_upper_rack` | grasp |
| `l_kitchen_two_long_legs_dishwasher_upper_rack_volume` | `l_kitchen_two_long_legs_dishwasher_upper_rack` | container_volume |
| `l_kitchen_two_long_legs_b4_pullout_grip` | `l_kitchen_two_long_legs_b4_pullout` | grasp |
| `l_kitchen_two_long_legs_b4_pullout_volume` | `l_kitchen_two_long_legs_b4_pullout` | container_volume |
| `l_kitchen_two_long_legs_w1_left_door_grip` | `l_kitchen_two_long_legs_w1_left_door` | grasp |
| `l_kitchen_two_long_legs_w1_right_door_grip` | `l_kitchen_two_long_legs_w1_right_door` | grasp |
| `l_kitchen_two_long_legs_w2_left_glass_door_grip` | `l_kitchen_two_long_legs_w2_left_glass_door` | grasp |
| `l_kitchen_two_long_legs_w2_right_glass_door_grip` | `l_kitchen_two_long_legs_w2_right_glass_door` | grasp |
| `l_kitchen_two_long_legs_w3_glass_door_grip` | `l_kitchen_two_long_legs_w3_glass_door` | grasp |
| `l_kitchen_two_long_legs_w4_shelf_surface` | `l_kitchen_two_long_legs_body` | place_surface |
| `l_kitchen_two_long_legs_freezer_door_grip` | `l_kitchen_two_long_legs_freezer_door` | grasp |
| `l_kitchen_two_long_legs_fridge_door_grip` | `l_kitchen_two_long_legs_fridge_door` | grasp |
| `l_kitchen_two_long_legs_rb1_top_door_grip` | `l_kitchen_two_long_legs_rb1_top_door` | grasp |
| `l_kitchen_two_long_legs_freezer_drawer_1_volume` | `l_kitchen_two_long_legs_freezer_drawer_1` | container_volume |
| `l_kitchen_two_long_legs_freezer_drawer_1_grip` | `l_kitchen_two_long_legs_freezer_drawer_1` | grasp |
| `l_kitchen_two_long_legs_freezer_drawer_2_volume` | `l_kitchen_two_long_legs_freezer_drawer_2` | container_volume |
| `l_kitchen_two_long_legs_freezer_drawer_2_grip` | `l_kitchen_two_long_legs_freezer_drawer_2` | grasp |
| `l_kitchen_two_long_legs_fridge_volume` | `l_kitchen_two_long_legs_body` | container_volume |
| `l_kitchen_two_long_legs_rb2_door_grip` | `l_kitchen_two_long_legs_rb2_door` | grasp |
| `l_kitchen_two_long_legs_oven_storage_drawer_grip` | `l_kitchen_two_long_legs_oven_storage_drawer` | grasp |
| `l_kitchen_two_long_legs_oven_storage_drawer_volume` | `l_kitchen_two_long_legs_oven_storage_drawer` | container_volume |
| `l_kitchen_two_long_legs_oven_cavity_volume` | `l_kitchen_two_long_legs_body` | container_volume |
| `l_kitchen_two_long_legs_oven_knob_1_contact` | `l_kitchen_two_long_legs_oven_knob_1` | control |
| `l_kitchen_two_long_legs_oven_knob_2_contact` | `l_kitchen_two_long_legs_oven_knob_2` | control |
| `l_kitchen_two_long_legs_oven_door_grip` | `l_kitchen_two_long_legs_oven_door` | grasp |
| `l_kitchen_two_long_legs_hob_surface` | `l_kitchen_two_long_legs_body` | place_surface |
| `l_kitchen_two_long_legs_rb4_top_drawer_grip` | `l_kitchen_two_long_legs_rb4_top_drawer` | grasp |
| `l_kitchen_two_long_legs_rb4_top_drawer_volume` | `l_kitchen_two_long_legs_rb4_top_drawer` | container_volume |
| `l_kitchen_two_long_legs_rb4_middle_drawer_grip` | `l_kitchen_two_long_legs_rb4_middle_drawer` | grasp |
| `l_kitchen_two_long_legs_rb4_middle_drawer_volume` | `l_kitchen_two_long_legs_rb4_middle_drawer` | container_volume |
| `l_kitchen_two_long_legs_rb4_bottom_drawer_grip` | `l_kitchen_two_long_legs_rb4_bottom_drawer` | grasp |
| `l_kitchen_two_long_legs_rb4_bottom_drawer_volume` | `l_kitchen_two_long_legs_rb4_bottom_drawer` | container_volume |
| `l_kitchen_two_long_legs_rw2_flap_grip` | `l_kitchen_two_long_legs_rw2_flap` | grasp |
| `l_kitchen_two_long_legs_hood_visor_grip` | `l_kitchen_two_long_legs_hood_visor` | grasp |
| `l_kitchen_two_long_legs_rw3_flap_grip` | `l_kitchen_two_long_legs_rw3_flap` | grasp |
| `l_kitchen_two_long_legs_rw4_door_grip` | `l_kitchen_two_long_legs_rw4_door` | grasp |
| `l_kitchen_two_long_legs_worktop_surface` | `l_kitchen_two_long_legs_body` | place_surface |
| `l_kitchen_two_long_legs_return_worktop_surface` | `l_kitchen_two_long_legs_body` | place_surface |
| `l_kitchen_two_long_legs_wall_anchor` | `l_kitchen_two_long_legs_body` | wall_mount |
| `l_kitchen_two_long_legs_return_wall_anchor` | `l_kitchen_two_long_legs_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model cooking heat, refrigeration, water supply and drainage, dishwasher cycles, hinge dampers, drawer runners, load ratings, wall-fixing strength or assembly.
