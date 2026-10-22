# Soldering Station with Iron Holder

Temperature-controlled soldering station beside a weighted holder: the iron cradle tilts, the sponge tray slides out, with a knob and a power rocker.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing, base and tray wall plus boxes around the holder coil, so the coil and tray stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `soldering_station_iron_cradle_joint` | revolute | 0.55 |
| `soldering_station_sponge_tray_joint` | prismatic | 0.05 |
| `soldering_station_temperature_knob_joint` | revolute | 2.4 |
| `soldering_station_power_switch_joint` | revolute | 0.3 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `soldering_station_iron_handle_grip` | `soldering_station_iron_cradle` | grasp |
| `soldering_station_temperature_knob_contact` | `soldering_station_temperature_knob` | control |
| `soldering_station_power_switch_contact` | `soldering_station_power_switch` | control |
| `soldering_station_sponge_tray_grip` | `soldering_station_sponge_tray` | grasp |
| `soldering_station_sponge_tray_volume` | `soldering_station_sponge_tray` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model heating, temperature control, the iron cable, the sponge or solder.
