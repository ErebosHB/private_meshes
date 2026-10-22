# Oxy-Fuel Cutting Torch

Gas cutting torch lying on its side, with a cutting-oxygen lever, three valve knobs and a right-angle cutting head.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level under the torch, with the torch lying on its side.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per handle, tube, valve block, head and hose segment.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `oxy_fuel_cutting_torch_cutting_lever_joint` | revolute | 0.24 |
| `oxy_fuel_cutting_torch_oxygen_valve_joint` | revolute | 2.4 |
| `oxy_fuel_cutting_torch_fuel_valve_joint` | revolute | 2 |
| `oxy_fuel_cutting_torch_preheat_valve_joint` | revolute | 1.6 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `oxy_fuel_cutting_torch_handle_grip` | `oxy_fuel_cutting_torch_body` | grasp |
| `oxy_fuel_cutting_torch_cutting_lever_tip` | `oxy_fuel_cutting_torch_cutting_lever` | control |
| `oxy_fuel_cutting_torch_oxygen_valve_contact` | `oxy_fuel_cutting_torch_oxygen_valve` | control |
| `oxy_fuel_cutting_torch_fuel_valve_contact` | `oxy_fuel_cutting_torch_fuel_valve` | control |
| `oxy_fuel_cutting_torch_nozzle_tip` | `oxy_fuel_cutting_torch_body` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model gas flow, flame, flashback arrestors, valve seats or hose flex.
