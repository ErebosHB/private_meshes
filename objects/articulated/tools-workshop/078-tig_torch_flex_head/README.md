# TIG Torch with Flexible Head

Gas-shielded tungsten torch lying on its side, with a bendable head, a pull-out back cap, a gas valve and a thumb button.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level under the torch, with the torch lying on its side.
Use a unique URDF parser prefix for each instance.
Collision uses one cylinder per handle, neck, head, cup and hose segment.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `tig_torch_flex_head_flex_head_joint` | revolute | 0.8 |
| `tig_torch_flex_head_back_cap_joint` | prismatic | 0.025 |
| `tig_torch_flex_head_gas_valve_joint` | revolute | 2.4 |
| `tig_torch_flex_head_torch_button_joint` | prismatic | 0.002 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `tig_torch_flex_head_handle_grip` | `tig_torch_flex_head_body` | grasp |
| `tig_torch_flex_head_torch_button_contact` | `tig_torch_flex_head_torch_button` | control |
| `tig_torch_flex_head_gas_valve_contact` | `tig_torch_flex_head_gas_valve` | control |
| `tig_torch_flex_head_electrode_tip` | `tig_torch_flex_head_flex_head` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the arc, shielding gas flow, cooling, the button switch or hose flex.
