# Air Fryer

Countertop hot-air fryer with a pull-out basket drawer, a timer dial and a basket release button.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing wall and thin boxes for the pan and basket walls, so the cooking chamber and basket stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; glass 2,500; rubber 1,100; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `air_fryer_timer_dial_joint` | revolute | 1.57 |
| `air_fryer_basket_drawer_joint` | prismatic | 0.18 |
| `air_fryer_release_button_joint` | prismatic | 0.003 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `air_fryer_timer_dial_contact` | `air_fryer_timer_dial` | control |
| `air_fryer_release_button_contact` | `air_fryer_release_button` | control |
| `air_fryer_basket_drawer_grip` | `air_fryer_basket_drawer` | grasp |
| `air_fryer_basket_volume` | `air_fryer_basket_drawer` | container_volume |
| `air_fryer_top_surface` | `air_fryer_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model heating, the fan, airflow, the basket-release latch's lock or load ratings.
