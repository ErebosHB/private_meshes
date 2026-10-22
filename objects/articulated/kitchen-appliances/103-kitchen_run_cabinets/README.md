# Kitchen Run, Cabinets Only

2.7 m cabinet run with sink, an open dishwasher niche, an oven housing with drawer and a narrow pull-out, ready for own appliances.

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
| `kitchen_run_cabinets_b1_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_cabinets_b1_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_sink_left_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_sink_right_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_b4_drawer_joint` | prismatic | 0.276 |
| `kitchen_run_cabinets_b5_pullout_joint` | prismatic | 0.276 |
| `kitchen_run_cabinets_w1_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_w2_left_glass_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_w2_right_glass_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_w3_glass_door_joint` | revolute | 1.4 |
| `kitchen_run_cabinets_w4_flap_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `kitchen_run_cabinets_b1_drawer_grip` | `kitchen_run_cabinets_b1_drawer` | grasp |
| `kitchen_run_cabinets_b1_drawer_volume` | `kitchen_run_cabinets_b1_drawer` | container_volume |
| `kitchen_run_cabinets_b1_door_grip` | `kitchen_run_cabinets_b1_door` | grasp |
| `kitchen_run_cabinets_sink_left_door_grip` | `kitchen_run_cabinets_sink_left_door` | grasp |
| `kitchen_run_cabinets_sink_right_door_grip` | `kitchen_run_cabinets_sink_right_door` | grasp |
| `kitchen_run_cabinets_sink_basin_volume` | `kitchen_run_cabinets_body` | container_volume |
| `kitchen_run_cabinets_b3_appliance_niche_volume` | `kitchen_run_cabinets_body` | container_volume |
| `kitchen_run_cabinets_b4_drawer_grip` | `kitchen_run_cabinets_b4_drawer` | grasp |
| `kitchen_run_cabinets_b4_drawer_volume` | `kitchen_run_cabinets_b4_drawer` | container_volume |
| `kitchen_run_cabinets_b4_oven_niche_volume` | `kitchen_run_cabinets_body` | container_volume |
| `kitchen_run_cabinets_b5_pullout_grip` | `kitchen_run_cabinets_b5_pullout` | grasp |
| `kitchen_run_cabinets_b5_pullout_volume` | `kitchen_run_cabinets_b5_pullout` | container_volume |
| `kitchen_run_cabinets_w1_door_grip` | `kitchen_run_cabinets_w1_door` | grasp |
| `kitchen_run_cabinets_w2_left_glass_door_grip` | `kitchen_run_cabinets_w2_left_glass_door` | grasp |
| `kitchen_run_cabinets_w2_right_glass_door_grip` | `kitchen_run_cabinets_w2_right_glass_door` | grasp |
| `kitchen_run_cabinets_w3_glass_door_grip` | `kitchen_run_cabinets_w3_glass_door` | grasp |
| `kitchen_run_cabinets_w4_flap_grip` | `kitchen_run_cabinets_w4_flap` | grasp |
| `kitchen_run_cabinets_w4_hood_niche_volume` | `kitchen_run_cabinets_body` | container_volume |
| `kitchen_run_cabinets_w5_shelf_surface` | `kitchen_run_cabinets_body` | place_surface |
| `kitchen_run_cabinets_worktop_surface` | `kitchen_run_cabinets_body` | place_surface |
| `kitchen_run_cabinets_wall_anchor` | `kitchen_run_cabinets_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model appliance installation, water connection, hinge dampers, drawer runners, load ratings, wall-fixing strength or assembly.
