# Pressure Washer

Upright high-pressure cleaner on two wheels, with a telescoping handle, a front hose reel with crank and a main switch.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, wheel, reel flange and handle tube, so the gap between reel and housing stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `pressure_washer_wheel_1_joint` | continuous | 0 |
| `pressure_washer_wheel_2_joint` | continuous | 0 |
| `pressure_washer_hose_reel_joint` | continuous | 1.6 |
| `pressure_washer_handle_joint` | prismatic | 0.28 |
| `pressure_washer_main_switch_joint` | revolute | 1.57 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `pressure_washer_handle_grip` | `pressure_washer_handle` | grasp |
| `pressure_washer_reel_crank_knob` | `pressure_washer_hose_reel` | grasp |
| `pressure_washer_main_switch_contact` | `pressure_washer_main_switch` | control |
| `pressure_washer_high_pressure_outlet` | `pressure_washer_body` | tool_attachment |
| `pressure_washer_gun_holster_slot` | `pressure_washer_body` | container_volume |
| `pressure_washer_anti_tip_anchor` | `pressure_washer_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model pump pressure, water flow, detergent dosing, the trigger gun, hose flexibility or water.
