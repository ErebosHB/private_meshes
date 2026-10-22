# Shoe Cabinet with Tip-out Compartments

Shallow shoe cabinet with two tip-out compartments.

Original concept model by Yannick Schröder.
Typology drawn from a public furniture catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so both compartments stay open behind their tip-out fronts.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `shoe_cabinet_tipout_lower_compartment_joint` | revolute | 0.55 |
| `shoe_cabinet_tipout_upper_compartment_joint` | revolute | 0.55 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `shoe_cabinet_tipout_lower_compartment_grip` | `shoe_cabinet_tipout_lower_compartment` | grasp |
| `shoe_cabinet_tipout_lower_compartment_volume` | `shoe_cabinet_tipout_lower_compartment` | container_volume |
| `shoe_cabinet_tipout_upper_compartment_grip` | `shoe_cabinet_tipout_upper_compartment` | grasp |
| `shoe_cabinet_tipout_upper_compartment_volume` | `shoe_cabinet_tipout_upper_compartment` | container_volume |
| `shoe_cabinet_tipout_top_surface` | `shoe_cabinet_tipout_body` | place_surface |
| `shoe_cabinet_tipout_wall_anchor` | `shoe_cabinet_tipout_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model tip-out stops, load ratings, wall-fixing strength, assembly or tip-over behaviour.
