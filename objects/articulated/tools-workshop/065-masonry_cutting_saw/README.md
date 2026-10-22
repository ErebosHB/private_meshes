# Masonry Cutting Saw

Wet-cut block saw on a wheeled stand: a carriage slides along the rails under a saw head that pivots down onto the work.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per leg, rail, tray wall, arm part and the blade, so the cutting gap and the water tray stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `masonry_cutting_saw_wheel_1_joint` | continuous | 0 |
| `masonry_cutting_saw_wheel_2_joint` | continuous | 0 |
| `masonry_cutting_saw_carriage_joint` | prismatic | 0.26 |
| `masonry_cutting_saw_saw_head_joint` | revolute | 0.32 |
| `masonry_cutting_saw_blade_spindle_joint` | continuous | 0 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `masonry_cutting_saw_head_grip` | `masonry_cutting_saw_saw_head` | grasp |
| `masonry_cutting_saw_push_grip` | `masonry_cutting_saw_carriage` | grasp |
| `masonry_cutting_saw_cutting_table_surface` | `masonry_cutting_saw_carriage` | place_surface |
| `masonry_cutting_saw_blade_edge` | `masonry_cutting_saw_saw_head` | tool_attachment |
| `masonry_cutting_saw_water_tray_volume` | `masonry_cutting_saw_body` | container_volume |
| `masonry_cutting_saw_column_anchor` | `masonry_cutting_saw_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the wet-cut water pump, blade cooling, cutting forces, dust, blade wear or tip-over behaviour.
