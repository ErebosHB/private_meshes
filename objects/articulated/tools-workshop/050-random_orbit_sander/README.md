# Random Orbit Sander

Palm sander on a 125 mm pad with a slide-off dust box, power switch and speed wheel.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, the pad and the dust box walls, so the dust box stays open once removed.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `random_orbit_sander_pad_joint` | continuous | 0.9 |
| `random_orbit_sander_dust_box_joint` | prismatic | 0.06 |
| `random_orbit_sander_power_switch_joint` | prismatic | 0.006 |
| `random_orbit_sander_speed_wheel_joint` | revolute | 2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `random_orbit_sander_palm_grip` | `random_orbit_sander_body` | grasp |
| `random_orbit_sander_dust_box_grip` | `random_orbit_sander_dust_box` | grasp |
| `random_orbit_sander_dust_box_volume` | `random_orbit_sander_dust_box` | container_volume |
| `random_orbit_sander_power_switch_contact` | `random_orbit_sander_power_switch` | control |
| `random_orbit_sander_speed_wheel_contact` | `random_orbit_sander_speed_wheel` | control |
| `random_orbit_sander_abrasive_face` | `random_orbit_sander_pad` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the eccentric orbit, pad brake, dust extraction airflow, abrasive grit or vibration.
