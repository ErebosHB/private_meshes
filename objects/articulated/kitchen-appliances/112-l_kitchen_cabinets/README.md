# L-Shaped Kitchen, Cabinets Only

Low corner cabinet run, 3.1 m by 2.0 m, with corner cupboard, sink, an open dishwasher niche, wide drawers, an oven housing and a double cupboard.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per carcass panel, front, worktop piece and appliance wall, so every cupboard, drawer, niche, basin and appliance cavity stays open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; glass 2,500; particleboard 650; pine 500; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `l_kitchen_cabinets_b1_corner_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_b1_corner_basket_joint` | prismatic | 0.264 |
| `l_kitchen_cabinets_sink_left_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_sink_right_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_b4_top_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_cabinets_b4_middle_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_cabinets_b4_bottom_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_cabinets_w1_left_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_w1_right_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_w2_left_glass_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_w2_right_glass_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_w3_glass_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_w4_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_rb1_drawer_joint` | prismatic | 0.276 |
| `l_kitchen_cabinets_rb2_left_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_rb2_right_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_rw1_flap_joint` | revolute | 1.2 |
| `l_kitchen_cabinets_rw2_left_glass_door_joint` | revolute | 1.4 |
| `l_kitchen_cabinets_rw2_right_glass_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `l_kitchen_cabinets_b1_corner_door_grip` | `l_kitchen_cabinets_b1_corner_door` | grasp |
| `l_kitchen_cabinets_b1_corner_basket_volume` | `l_kitchen_cabinets_b1_corner_basket` | container_volume |
| `l_kitchen_cabinets_b1_corner_basket_grip` | `l_kitchen_cabinets_b1_corner_basket` | grasp |
| `l_kitchen_cabinets_sink_left_door_grip` | `l_kitchen_cabinets_sink_left_door` | grasp |
| `l_kitchen_cabinets_sink_right_door_grip` | `l_kitchen_cabinets_sink_right_door` | grasp |
| `l_kitchen_cabinets_sink_basin_volume` | `l_kitchen_cabinets_body` | container_volume |
| `l_kitchen_cabinets_b3_appliance_niche_volume` | `l_kitchen_cabinets_body` | container_volume |
| `l_kitchen_cabinets_b4_top_drawer_grip` | `l_kitchen_cabinets_b4_top_drawer` | grasp |
| `l_kitchen_cabinets_b4_top_drawer_volume` | `l_kitchen_cabinets_b4_top_drawer` | container_volume |
| `l_kitchen_cabinets_b4_middle_drawer_grip` | `l_kitchen_cabinets_b4_middle_drawer` | grasp |
| `l_kitchen_cabinets_b4_middle_drawer_volume` | `l_kitchen_cabinets_b4_middle_drawer` | container_volume |
| `l_kitchen_cabinets_b4_bottom_drawer_grip` | `l_kitchen_cabinets_b4_bottom_drawer` | grasp |
| `l_kitchen_cabinets_b4_bottom_drawer_volume` | `l_kitchen_cabinets_b4_bottom_drawer` | container_volume |
| `l_kitchen_cabinets_w1_left_door_grip` | `l_kitchen_cabinets_w1_left_door` | grasp |
| `l_kitchen_cabinets_w1_right_door_grip` | `l_kitchen_cabinets_w1_right_door` | grasp |
| `l_kitchen_cabinets_w2_left_glass_door_grip` | `l_kitchen_cabinets_w2_left_glass_door` | grasp |
| `l_kitchen_cabinets_w2_right_glass_door_grip` | `l_kitchen_cabinets_w2_right_glass_door` | grasp |
| `l_kitchen_cabinets_w3_glass_door_grip` | `l_kitchen_cabinets_w3_glass_door` | grasp |
| `l_kitchen_cabinets_w4_door_grip` | `l_kitchen_cabinets_w4_door` | grasp |
| `l_kitchen_cabinets_rb1_drawer_grip` | `l_kitchen_cabinets_rb1_drawer` | grasp |
| `l_kitchen_cabinets_rb1_drawer_volume` | `l_kitchen_cabinets_rb1_drawer` | container_volume |
| `l_kitchen_cabinets_rb1_oven_niche_volume` | `l_kitchen_cabinets_body` | container_volume |
| `l_kitchen_cabinets_rb2_left_door_grip` | `l_kitchen_cabinets_rb2_left_door` | grasp |
| `l_kitchen_cabinets_rb2_right_door_grip` | `l_kitchen_cabinets_rb2_right_door` | grasp |
| `l_kitchen_cabinets_rw1_flap_grip` | `l_kitchen_cabinets_rw1_flap` | grasp |
| `l_kitchen_cabinets_rw1_hood_niche_volume` | `l_kitchen_cabinets_body` | container_volume |
| `l_kitchen_cabinets_rw2_left_glass_door_grip` | `l_kitchen_cabinets_rw2_left_glass_door` | grasp |
| `l_kitchen_cabinets_rw2_right_glass_door_grip` | `l_kitchen_cabinets_rw2_right_glass_door` | grasp |
| `l_kitchen_cabinets_worktop_surface` | `l_kitchen_cabinets_body` | place_surface |
| `l_kitchen_cabinets_return_worktop_surface` | `l_kitchen_cabinets_body` | place_surface |
| `l_kitchen_cabinets_wall_anchor` | `l_kitchen_cabinets_body` | wall_mount |
| `l_kitchen_cabinets_return_wall_anchor` | `l_kitchen_cabinets_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model appliance installation, water connection, hinge dampers, drawer runners, load ratings, wall-fixing strength or assembly.
