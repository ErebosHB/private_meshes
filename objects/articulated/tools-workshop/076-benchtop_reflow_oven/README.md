# Benchtop Reflow Oven

Drawer-type soldering oven for circuit boards with a windowed pull-out tray, a display and a start button.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing wall and tray wall, so the oven bay and the tray stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `benchtop_reflow_oven_drawer_joint` | prismatic | 0.18 |
| `benchtop_reflow_oven_start_button_joint` | prismatic | 0.004 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `benchtop_reflow_oven_drawer_handle_grip` | `benchtop_reflow_oven_drawer` | grasp |
| `benchtop_reflow_oven_drawer_tray_volume` | `benchtop_reflow_oven_drawer` | container_volume |
| `benchtop_reflow_oven_start_button_contact` | `benchtop_reflow_oven_start_button` | control |
| `benchtop_reflow_oven_top_surface` | `benchtop_reflow_oven_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model the heaters, temperature profiles, airflow, solder paste or board loading.
