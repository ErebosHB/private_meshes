# Heat Gun

Pistol-grip hot-air gun standing on its heel, with a fold-down wire stand, rocker switch and temperature wheel.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, nozzle and wire segment, so the gap under the barrel stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `heat_gun_rocker_switch_joint` | revolute | 0.35 |
| `heat_gun_temperature_wheel_joint` | revolute | 2.1 |
| `heat_gun_stand_joint` | revolute | 1.42 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `heat_gun_handle_grip` | `heat_gun_body` | grasp |
| `heat_gun_rocker_switch_contact` | `heat_gun_rocker_switch` | control |
| `heat_gun_temperature_wheel_contact` | `heat_gun_temperature_wheel` | control |
| `heat_gun_nozzle_outlet` | `heat_gun_body` | tool_attachment |
| `heat_gun_stand_foot_grip` | `heat_gun_stand` | grasp |

The URDF supplies geometry, articulation and frames. It does not model air temperature, airflow, the heating element, overheat cut-off, nozzle attachments or burn hazards.
