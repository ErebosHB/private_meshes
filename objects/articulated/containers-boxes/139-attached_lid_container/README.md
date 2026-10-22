# Attached-Lid Container

Stackable plastic tote whose two lid halves hinge open from the long top edges.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per wall, floor panel and lid plate, so the tote stays open when the lids are raised.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; ABS/HDPE 1,050 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `attached_lid_container_front_lid_joint` | revolute | 1.2 |
| `attached_lid_container_back_lid_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `attached_lid_container_tote_volume` | `attached_lid_container_body` | container_volume |
| `attached_lid_container_left_handle_grip` | `attached_lid_container_body` | grasp |
| `attached_lid_container_right_handle_grip` | `attached_lid_container_body` | grasp |
| `attached_lid_container_front_lid_grip` | `attached_lid_container_front_lid` | grasp |
| `attached_lid_container_back_lid_grip` | `attached_lid_container_back_lid` | grasp |

The URDF supplies geometry, articulation and frames. It does not model lid interlock teeth, seal tags, nesting or stacking loads, or load ratings.
