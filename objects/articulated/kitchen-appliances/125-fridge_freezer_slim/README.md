# Fridge-Freezer, Slim Depth

Narrow, shallow fridge-freezer with two right-hinged doors, glass fridge shelves and two freezer drawers.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing, liner, shelf and drawer panel, so both compartments and the drawers stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; glass 2,500; particleboard 650; rubber 1,100 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `fridge_freezer_slim_freezer_door_joint` | revolute | 1.4 |
| `fridge_freezer_slim_fridge_door_joint` | revolute | 1.4 |
| `fridge_freezer_slim_freezer_drawer_1_joint` | prismatic | 0.216 |
| `fridge_freezer_slim_freezer_drawer_2_joint` | prismatic | 0.216 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `fridge_freezer_slim_freezer_door_grip` | `fridge_freezer_slim_freezer_door` | grasp |
| `fridge_freezer_slim_fridge_door_grip` | `fridge_freezer_slim_fridge_door` | grasp |
| `fridge_freezer_slim_freezer_drawer_1_volume` | `fridge_freezer_slim_freezer_drawer_1` | container_volume |
| `fridge_freezer_slim_freezer_drawer_1_grip` | `fridge_freezer_slim_freezer_drawer_1` | grasp |
| `fridge_freezer_slim_freezer_drawer_2_volume` | `fridge_freezer_slim_freezer_drawer_2` | container_volume |
| `fridge_freezer_slim_freezer_drawer_2_grip` | `fridge_freezer_slim_freezer_drawer_2` | grasp |
| `fridge_freezer_slim_fridge_volume` | `fridge_freezer_slim_body` | container_volume |
| `fridge_freezer_slim_top_surface` | `fridge_freezer_slim_body` | place_surface |
| `fridge_freezer_slim_wall_anchor` | `fridge_freezer_slim_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model refrigeration, the door seals, defrosting, load ratings or tip-over behaviour.
