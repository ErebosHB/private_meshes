# Under-Counter Freezer

Table-height freezer with a right-hinged door over three pull-out freezer baskets.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing, liner and basket panel, so the compartment and each basket stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; particleboard 650; rubber 1,100 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `under_counter_freezer_door_joint` | revolute | 1.4 |
| `under_counter_freezer_basket_1_joint` | prismatic | 0.24 |
| `under_counter_freezer_basket_2_joint` | prismatic | 0.24 |
| `under_counter_freezer_basket_3_joint` | prismatic | 0.24 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `under_counter_freezer_door_grip` | `under_counter_freezer_door` | grasp |
| `under_counter_freezer_basket_1_volume` | `under_counter_freezer_basket_1` | container_volume |
| `under_counter_freezer_basket_1_grip` | `under_counter_freezer_basket_1` | grasp |
| `under_counter_freezer_basket_2_volume` | `under_counter_freezer_basket_2` | container_volume |
| `under_counter_freezer_basket_2_grip` | `under_counter_freezer_basket_2` | grasp |
| `under_counter_freezer_basket_3_volume` | `under_counter_freezer_basket_3` | container_volume |
| `under_counter_freezer_basket_3_grip` | `under_counter_freezer_basket_3` | grasp |
| `under_counter_freezer_freezer_volume` | `under_counter_freezer_body` | container_volume |
| `under_counter_freezer_top_surface` | `under_counter_freezer_body` | place_surface |
| `under_counter_freezer_wall_anchor` | `under_counter_freezer_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model refrigeration, the door seal, defrosting, load ratings or tip-over behaviour.
