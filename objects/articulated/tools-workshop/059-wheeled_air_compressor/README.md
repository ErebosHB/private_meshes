# Wheeled Air Compressor

Horizontal-tank compressor on two wheels with a telescoping pull handle, pressure regulator, gauges and power switch.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per tank, pump block, frame bar, wheel and handle tube, so the space under the tank stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wheeled_air_compressor_wheel_1_joint` | continuous | 0 |
| `wheeled_air_compressor_wheel_2_joint` | continuous | 0 |
| `wheeled_air_compressor_pull_handle_joint` | prismatic | 0.3 |
| `wheeled_air_compressor_regulator_knob_joint` | revolute | 2.2 |
| `wheeled_air_compressor_power_switch_joint` | revolute | 1.57 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wheeled_air_compressor_pull_handle_grip` | `wheeled_air_compressor_pull_handle` | grasp |
| `wheeled_air_compressor_regulator_knob_contact` | `wheeled_air_compressor_regulator_knob` | control |
| `wheeled_air_compressor_power_switch_contact` | `wheeled_air_compressor_power_switch` | control |
| `wheeled_air_compressor_air_coupler` | `wheeled_air_compressor_body` | tool_attachment |
| `wheeled_air_compressor_pump_cover_surface` | `wheeled_air_compressor_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model air delivery, tank pressure, the safety valve, the pressure switch cut-in and cut-out, condensate or motor heat.
