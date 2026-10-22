# Two-Component Cartridge Gun

Manual dispenser lying on its side with a twin cartridge and static mixer: the twin plunger advances, with a trigger and a release lever.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint, with the gun lying on its side.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per cartridge, yoke, rail, housing, handle and plunger part.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `two_component_cartridge_gun_plunger_joint` | prismatic | 0.15 |
| `two_component_cartridge_gun_trigger_joint` | revolute | 0.3 |
| `two_component_cartridge_gun_release_lever_joint` | revolute | 0.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `two_component_cartridge_gun_handle_grip` | `two_component_cartridge_gun_body` | grasp |
| `two_component_cartridge_gun_trigger_contact` | `two_component_cartridge_gun_trigger` | control |
| `two_component_cartridge_gun_cartridge_volume` | `two_component_cartridge_gun_body` | container_volume |
| `two_component_cartridge_gun_mixer_tip` | `two_component_cartridge_gun_body` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the ratchet drive, mixing ratio, adhesive flow, cartridge pressure or curing.
