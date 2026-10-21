# Two-Sided Tote Shelving

Shallow boltless shelving bay open on both faces, with a low tote level that robots load from one side and unload from the other.

Original concept model by Vanessa Hassouna, developed for AICOR Solutions.
Typology drawn from a public product reference; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint; both long faces are open.
Use a unique URDF parser prefix for each instance.
Collision uses one box per upright, beam and deck, so every level stays open from both faces.
Masses/inertias are approximate model parameters from primitive volumes, not manufacturer specifications.

## Moving parts

The body is a single rigid link; the object has no moving parts, so the rest and inspection renders are the same.

| Joint | Motion | Inspection position |
| --- | --- | --- |
| none | - | - |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `two_sided_tote_shelving_robot_level_surface` | `two_sided_tote_shelving_body` | place_surface |
| `two_sided_tote_shelving_manual_deck_surface` | `two_sided_tote_shelving_body` | place_surface |
| `two_sided_tote_shelving_top_surface` | `two_sided_tote_shelving_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model deck load ratings, beam locking pins, floor anchoring or tip-over behaviour.
