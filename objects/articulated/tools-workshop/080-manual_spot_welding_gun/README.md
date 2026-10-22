# Manual Spot Welding Gun

Scissor-type spot welding gun lying flat: the upper arm pivots open on a lever, the lower arm and transformer housing are fixed.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint, with the gun lying flat.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing, arm, handle and cable segment, so the gap between the arms stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `manual_spot_welding_gun_upper_arm_joint` | revolute | 0.3 |
| `manual_spot_welding_gun_trigger_joint` | prismatic | 0.004 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `manual_spot_welding_gun_fixed_handle_grip` | `manual_spot_welding_gun_body` | grasp |
| `manual_spot_welding_gun_lever_grip` | `manual_spot_welding_gun_upper_arm` | grasp |
| `manual_spot_welding_gun_trigger_contact` | `manual_spot_welding_gun_trigger` | control |
| `manual_spot_welding_gun_upper_electrode_tip` | `manual_spot_welding_gun_upper_arm` | tool_attachment |
| `manual_spot_welding_gun_lower_electrode_tip` | `manual_spot_welding_gun_body` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the transformer, electrode force, weld current or timing, cooling or cable flex.
