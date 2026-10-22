# Submersible Pump

Drainage pump on a slotted strainer base, with a fold-up carry handle, an elbow outlet and a float switch on a swinging arm.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing section, outlet segment and handle bar plus a ring of boxes for the strainer, so the intake stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `submersible_pump_carry_handle_joint` | revolute | 1.45 |
| `submersible_pump_float_switch_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `submersible_pump_carry_handle_grip` | `submersible_pump_carry_handle` | grasp |
| `submersible_pump_float_switch_body` | `submersible_pump_float_switch` | control |
| `submersible_pump_hose_outlet` | `submersible_pump_body` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model flow rate, delivery head, the impeller, dry-run protection, the float cable's flexibility or water.
