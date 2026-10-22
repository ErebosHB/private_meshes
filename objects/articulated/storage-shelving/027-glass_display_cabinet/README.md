# Glass Display Cabinet

Narrow steel-framed display cabinet with glass sides, four glass shelves and a glass door.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per frame member, glass pane and shelf, so every display level stays open behind the door.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `glass_display_cabinet_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `glass_display_cabinet_door_grip` | `glass_display_cabinet_door` | grasp |
| `glass_display_cabinet_base_surface` | `glass_display_cabinet_body` | place_surface |
| `glass_display_cabinet_shelf_1_surface` | `glass_display_cabinet_body` | place_surface |
| `glass_display_cabinet_shelf_2_surface` | `glass_display_cabinet_body` | place_surface |
| `glass_display_cabinet_shelf_3_surface` | `glass_display_cabinet_body` | place_surface |
| `glass_display_cabinet_shelf_4_surface` | `glass_display_cabinet_body` | place_surface |
| `glass_display_cabinet_top_surface` | `glass_display_cabinet_body` | place_surface |
| `glass_display_cabinet_wall_anchor` | `glass_display_cabinet_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model glass breakage, interior lighting, the door lock, shelf load ratings or tip-over behaviour.
