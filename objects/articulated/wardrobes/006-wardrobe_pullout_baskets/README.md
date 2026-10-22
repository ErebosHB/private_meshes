# Wardrobe with Pull-out Wire Baskets

Narrow wardrobe with one hinged door, three pull-out wire baskets and two shelves.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so each basket stays open from above and the interior stays open behind the door.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wardrobe_pullout_baskets_door_joint` | revolute | 1.40 |
| `wardrobe_pullout_baskets_lower_basket_joint` | prismatic | 0.28 |
| `wardrobe_pullout_baskets_middle_basket_joint` | prismatic | 0.28 |
| `wardrobe_pullout_baskets_upper_basket_joint` | prismatic | 0.28 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wardrobe_pullout_baskets_door_grip` | `wardrobe_pullout_baskets_door` | grasp |
| `wardrobe_pullout_baskets_lower_basket_grip` | `wardrobe_pullout_baskets_lower_basket` | grasp |
| `wardrobe_pullout_baskets_lower_basket_volume` | `wardrobe_pullout_baskets_lower_basket` | container_volume |
| `wardrobe_pullout_baskets_middle_basket_grip` | `wardrobe_pullout_baskets_middle_basket` | grasp |
| `wardrobe_pullout_baskets_middle_basket_volume` | `wardrobe_pullout_baskets_middle_basket` | container_volume |
| `wardrobe_pullout_baskets_upper_basket_grip` | `wardrobe_pullout_baskets_upper_basket` | grasp |
| `wardrobe_pullout_baskets_upper_basket_volume` | `wardrobe_pullout_baskets_upper_basket` | container_volume |
| `wardrobe_pullout_baskets_lower_shelf_surface` | `wardrobe_pullout_baskets_body` | place_surface |
| `wardrobe_pullout_baskets_upper_shelf_surface` | `wardrobe_pullout_baskets_body` | place_surface |
| `wardrobe_pullout_baskets_wall_anchor` | `wardrobe_pullout_baskets_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model basket runners, hinge dampers, load ratings, wall-fixing strength, assembly or tip-over behaviour.
