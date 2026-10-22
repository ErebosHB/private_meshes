# Drum Sump Pallet with Hinged Grating

Steel sump pallet for two drums with fork pockets underneath; the grating hinges up at the back to empty the sump.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per sump wall, floor and skid, and a single slab for the grating, so the sump stays open when the grating is raised.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; steel grating as an equivalent 1,500 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `drum_sump_pallet_grating_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `drum_sump_pallet_sump_volume` | `drum_sump_pallet_body` | container_volume |
| `drum_sump_pallet_grating_front_grip` | `drum_sump_pallet_grating` | grasp |
| `drum_sump_pallet_grating_surface` | `drum_sump_pallet_grating` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model the sump capacity rating, liquid retention, grating load ratings, fork-lift handling or the drain plug.
