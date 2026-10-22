# MIG Welding Gun

Hand-held wire-feed welding torch lying on its side: a swivelling swan neck, a trigger and a slide-off gas nozzle.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level under the torch, with the gun lying on its side.
Use a unique URDF parser prefix for each instance.
Collision uses one cylinder per handle, neck and cable segment and boxes for the nozzle wall, so the nozzle bore stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `mig_welding_gun_swan_neck_joint` | revolute | 1.2 |
| `mig_welding_gun_gas_nozzle_joint` | prismatic | 0.03 |
| `mig_welding_gun_trigger_joint` | revolute | 0.28 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `mig_welding_gun_handle_grip` | `mig_welding_gun_body` | grasp |
| `mig_welding_gun_trigger_contact` | `mig_welding_gun_trigger` | control |
| `mig_welding_gun_contact_tip` | `mig_welding_gun_swan_neck` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model wire feed, shielding gas, the trigger switch, cable flex or arc heat.
