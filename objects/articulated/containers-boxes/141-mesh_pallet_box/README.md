# Mesh Pallet Box with Drop-down Flap

Stackable steel mesh box on pallet feet; the upper half of the front wall drops down for access.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one thin box per mesh wall, post, rail and foot, so the box stays open from above and the fork openings stay clear.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; hollow steel profiles as an equivalent 1,900 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `mesh_pallet_box_front_flap_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `mesh_pallet_box_box_volume` | `mesh_pallet_box_body` | container_volume |
| `mesh_pallet_box_top_rim_surface` | `mesh_pallet_box_body` | place_surface |
| `mesh_pallet_box_stack_anchor` | `mesh_pallet_box_body` | wall_mount |
| `mesh_pallet_box_front_flap_grip` | `mesh_pallet_box_front_flap` | grasp |

The URDF supplies geometry, articulation and frames. It does not model the flap latches, stacking loads and corner location, wire deflection or load ratings.
