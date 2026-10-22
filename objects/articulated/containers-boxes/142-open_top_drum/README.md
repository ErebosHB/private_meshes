# Open-Top Drum with Clamp Ring

Plastic open-top drum with two rolling hoops; a lever closes the clamp ring that holds the lid down.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses twelve wall slabs and a base disc for the drum, so the drum stays open from above when the lid is lifted.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; ABS/HDPE 1,050 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `open_top_drum_lid_joint` | prismatic | 0.25 |
| `open_top_drum_clamp_lever_joint` | revolute | 1.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `open_top_drum_drum_volume` | `open_top_drum_body` | container_volume |
| `open_top_drum_strap_anchor` | `open_top_drum_body` | wall_mount |
| `open_top_drum_lid_grip` | `open_top_drum_lid` | grasp |
| `open_top_drum_lid_top_surface` | `open_top_drum_lid` | place_surface |
| `open_top_drum_clamp_lever_tip` | `open_top_drum_clamp_lever` | control |

The URDF supplies geometry, articulation and frames. It does not model the lid gasket, clamp-ring tension, bung openings, liquid contents, drop behaviour or load ratings.
