# Fridge-Freezer

Tall fridge-freezer with a hinged fridge door carrying door bins, glass shelves and two pull-out freezer drawers.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing, liner, shelf and bin panel, so both compartments, the door bins and the drawers stay open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; enamelled steel 7,850; glass 2,500; rubber 1,100 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `fridge_freezer_upper_freezer_drawer_joint` | prismatic | 0.327 |
| `fridge_freezer_lower_freezer_drawer_joint` | prismatic | 0.327 |
| `fridge_freezer_fridge_door_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `fridge_freezer_upper_freezer_drawer_grip` | `fridge_freezer_upper_freezer_drawer` | grasp |
| `fridge_freezer_upper_freezer_drawer_volume` | `fridge_freezer_upper_freezer_drawer` | container_volume |
| `fridge_freezer_lower_freezer_drawer_grip` | `fridge_freezer_lower_freezer_drawer` | grasp |
| `fridge_freezer_lower_freezer_drawer_volume` | `fridge_freezer_lower_freezer_drawer` | container_volume |
| `fridge_freezer_fridge_door_grip` | `fridge_freezer_fridge_door` | grasp |
| `fridge_freezer_fridge_volume` | `fridge_freezer_body` | container_volume |
| `fridge_freezer_middle_shelf_surface` | `fridge_freezer_body` | place_surface |
| `fridge_freezer_wall_anchor` | `fridge_freezer_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model cooling, door seals and magnets, the door-closing damper, ice making or load ratings.
