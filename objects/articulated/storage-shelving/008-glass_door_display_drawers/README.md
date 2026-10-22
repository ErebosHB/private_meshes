# Glass-Door Display Cabinet with Drawers

Tall display cabinet with two glass doors over a base of three drawers.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so the display space stays open behind the glass doors and each drawer box stays hollow.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `glass_door_display_drawers_left_door_joint` | revolute | 1.40 |
| `glass_door_display_drawers_right_door_joint` | revolute | 1.40 |
| `glass_door_display_drawers_lower_drawer_joint` | prismatic | 0.21 |
| `glass_door_display_drawers_middle_drawer_joint` | prismatic | 0.21 |
| `glass_door_display_drawers_upper_drawer_joint` | prismatic | 0.21 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `glass_door_display_drawers_left_door_grip` | `glass_door_display_drawers_left_door` | grasp |
| `glass_door_display_drawers_right_door_grip` | `glass_door_display_drawers_right_door` | grasp |
| `glass_door_display_drawers_lower_drawer_grip` | `glass_door_display_drawers_lower_drawer` | grasp |
| `glass_door_display_drawers_lower_drawer_volume` | `glass_door_display_drawers_lower_drawer` | container_volume |
| `glass_door_display_drawers_middle_drawer_grip` | `glass_door_display_drawers_middle_drawer` | grasp |
| `glass_door_display_drawers_middle_drawer_volume` | `glass_door_display_drawers_middle_drawer` | container_volume |
| `glass_door_display_drawers_upper_drawer_grip` | `glass_door_display_drawers_upper_drawer` | grasp |
| `glass_door_display_drawers_upper_drawer_volume` | `glass_door_display_drawers_upper_drawer` | container_volume |
| `glass_door_display_drawers_display_floor_surface` | `glass_door_display_drawers_body` | place_surface |
| `glass_door_display_drawers_lower_shelf_surface` | `glass_door_display_drawers_body` | place_surface |
| `glass_door_display_drawers_upper_shelf_surface` | `glass_door_display_drawers_body` | place_surface |
| `glass_door_display_drawers_wall_anchor` | `glass_door_display_drawers_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model glass strength, hinge dampers, drawer runners, load ratings, wall-fixing strength, assembly or tip-over behaviour.
