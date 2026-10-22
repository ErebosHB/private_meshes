# Portable Inverter Welder

Compact stick/TIG welding inverter with a fold-up carry handle, a hinged cover over the front controls and a rear power rocker.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing block and end-frame bar plus cylinders for the handle, sockets and feet.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `portable_inverter_welder_carry_handle_joint` | revolute | 1.45 |
| `portable_inverter_welder_panel_cover_joint` | revolute | 1.2 |
| `portable_inverter_welder_current_knob_joint` | revolute | 2.4 |
| `portable_inverter_welder_power_switch_joint` | revolute | 0.3 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `portable_inverter_welder_carry_handle_grip` | `portable_inverter_welder_carry_handle` | grasp |
| `portable_inverter_welder_panel_cover_grip` | `portable_inverter_welder_panel_cover` | grasp |
| `portable_inverter_welder_current_knob_contact` | `portable_inverter_welder_current_knob` | control |
| `portable_inverter_welder_power_switch_contact` | `portable_inverter_welder_power_switch` | control |
| `portable_inverter_welder_top_surface` | `portable_inverter_welder_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model the inverter electronics, arc characteristics, duty cycle, cooling fan or welding cables.
