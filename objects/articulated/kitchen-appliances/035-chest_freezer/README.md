# Chest Freezer

Top-opening chest freezer with a counterbalanced lid, a sliding storage basket and a thermostat dial.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per insulated wall and thin boxes for the basket floor and walls, so the freezer well and basket stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; rubber 1,100; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `chest_freezer_thermostat_dial_joint` | revolute | 1.57 |
| `chest_freezer_basket_joint` | prismatic | 0.25 |
| `chest_freezer_lid_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `chest_freezer_thermostat_dial_contact` | `chest_freezer_thermostat_dial` | control |
| `chest_freezer_basket_grip` | `chest_freezer_basket` | grasp |
| `chest_freezer_basket_volume` | `chest_freezer_basket` | container_volume |
| `chest_freezer_lid_grip` | `chest_freezer_lid` | grasp |
| `chest_freezer_lid_top_surface` | `chest_freezer_lid` | place_surface |
| `chest_freezer_freezer_volume` | `chest_freezer_body` | container_volume |
| `chest_freezer_wall_anchor` | `chest_freezer_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model cooling, the lid's counterbalance hinges and seal, frost or load ratings.
