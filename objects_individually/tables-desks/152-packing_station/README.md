# Packing Station with Tote In-feed

Height-adjustable packing table with a drawer, a carton shelf above and a low in-feed shelf for delivered totes.

Original concept model by Vanessa Hassouna, developed for AICOR Solutions.
Typology drawn from a public product reference; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the worktop footprint; the in-feed shelf extends toward negative X.
Use a unique URDF parser prefix for each instance.
Collision uses boxes for the frame, worktop, shelves and drawer, so the drawer and the in-feed stay open.
Masses/inertias are approximate model parameters from primitive volumes, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `packing_station_worktop_joint` | prismatic | 0.27 |
| `packing_station_drawer_joint` | prismatic | 0.33 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `packing_station_infeed_surface` | `packing_station_body` | place_surface |
| `packing_station_carton_shelf_surface` | `packing_station_body` | place_surface |
| `packing_station_worktop_surface` | `packing_station_worktop` | place_surface |
| `packing_station_height_switch` | `packing_station_worktop` | control |
| `packing_station_drawer_grip` | `packing_station_drawer` | grasp |
| `packing_station_drawer_volume` | `packing_station_drawer` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model the lifting motor, its speed or load rating, the label printer or tape dispensing.
