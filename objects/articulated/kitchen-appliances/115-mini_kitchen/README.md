# Mini Kitchen

1.2 m compact kitchen with an under-counter fridge, a two-plate hob with front knobs, a sink cupboard and two wall cupboards.

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
| `mini_kitchen_hob_knob_1_joint` | revolute | 1.57 |
| `mini_kitchen_hob_knob_2_joint` | revolute | 1.57 |
| `mini_kitchen_fridge_door_joint` | revolute | 1.4 |
| `mini_kitchen_sink_left_door_joint` | revolute | 1.4 |
| `mini_kitchen_sink_right_door_joint` | revolute | 1.4 |
| `mini_kitchen_w1_flap_joint` | revolute | 1.2 |
| `mini_kitchen_w2_left_door_joint` | revolute | 1.4 |
| `mini_kitchen_w2_right_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `mini_kitchen_hob_knob_1_contact` | `mini_kitchen_hob_knob_1` | control |
| `mini_kitchen_hob_knob_2_contact` | `mini_kitchen_hob_knob_2` | control |
| `mini_kitchen_fridge_door_grip` | `mini_kitchen_fridge_door` | grasp |
| `mini_kitchen_fridge_volume` | `mini_kitchen_body` | container_volume |
| `mini_kitchen_sink_left_door_grip` | `mini_kitchen_sink_left_door` | grasp |
| `mini_kitchen_sink_right_door_grip` | `mini_kitchen_sink_right_door` | grasp |
| `mini_kitchen_sink_basin_volume` | `mini_kitchen_body` | container_volume |
| `mini_kitchen_w1_flap_grip` | `mini_kitchen_w1_flap` | grasp |
| `mini_kitchen_w2_left_door_grip` | `mini_kitchen_w2_left_door` | grasp |
| `mini_kitchen_w2_right_door_grip` | `mini_kitchen_w2_right_door` | grasp |
| `mini_kitchen_worktop_surface` | `mini_kitchen_body` | place_surface |
| `mini_kitchen_wall_anchor` | `mini_kitchen_body` | wall_mount |
| `mini_kitchen_hob_surface` | `mini_kitchen_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model cooking heat, refrigeration, water supply and drainage, dishwasher cycles, hinge dampers, drawer runners, load ratings, wall-fixing strength or assembly.
