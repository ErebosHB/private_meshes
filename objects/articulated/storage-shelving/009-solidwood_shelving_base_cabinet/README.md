# Solid-Wood Shelving with Base Cabinet

Solid-pine post shelving with open shelves above a two-door base cabinet.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so the cabinet stays open behind its doors and every shelf is reachable.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `solidwood_shelving_base_cabinet_left_door_joint` | revolute | 1.40 |
| `solidwood_shelving_base_cabinet_right_door_joint` | revolute | 1.40 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `solidwood_shelving_base_cabinet_left_door_grip` | `solidwood_shelving_base_cabinet_left_door` | grasp |
| `solidwood_shelving_base_cabinet_right_door_grip` | `solidwood_shelving_base_cabinet_right_door` | grasp |
| `solidwood_shelving_base_cabinet_cabinet_top_surface` | `solidwood_shelving_base_cabinet_body` | place_surface |
| `solidwood_shelving_base_cabinet_middle_shelf_surface` | `solidwood_shelving_base_cabinet_body` | place_surface |
| `solidwood_shelving_base_cabinet_top_surface` | `solidwood_shelving_base_cabinet_body` | place_surface |
| `solidwood_shelving_base_cabinet_wall_anchor` | `solidwood_shelving_base_cabinet_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model hinge dampers, shelf deflection, load ratings, wall-fixing strength, assembly or tip-over behaviour.
