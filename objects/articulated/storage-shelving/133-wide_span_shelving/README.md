# Wide-Span Shelving with Pull-out Shelf

Boltless wide-span steel shelving with three board decks and one deck that pulls out on telescopic rails.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per upright, beam, brace and deck, so every shelf level stays open from the front.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; hollow steel profiles as an equivalent 1,900; ABS/HDPE 1,050; particleboard 650 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wide_span_shelving_pullout_shelf_joint` | prismatic | 0.33 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wide_span_shelving_bottom_shelf_surface` | `wide_span_shelving_body` | place_surface |
| `wide_span_shelving_upper_shelf_surface` | `wide_span_shelving_body` | place_surface |
| `wide_span_shelving_top_surface` | `wide_span_shelving_body` | place_surface |
| `wide_span_shelving_wall_anchor` | `wide_span_shelving_body` | wall_mount |
| `wide_span_shelving_pullout_shelf_grip` | `wide_span_shelving_pullout_shelf` | grasp |
| `wide_span_shelving_pullout_shelf_surface` | `wide_span_shelving_pullout_shelf` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model the rail bearings, beam locking pins, load ratings per level, wall-fixing strength or tip-over behaviour.
