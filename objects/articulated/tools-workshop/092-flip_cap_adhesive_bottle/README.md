# Adhesive Bottle with Flip Cap

Small squeeze bottle for anaerobic or instant adhesives and thread lockers, with a nozzle under a hinged flip cap.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one cylinder each for the bottle, nozzle and cap.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `flip_cap_adhesive_bottle_flip_cap_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `flip_cap_adhesive_bottle_bottle_grip` | `flip_cap_adhesive_bottle_body` | grasp |
| `flip_cap_adhesive_bottle_flip_cap_lip` | `flip_cap_adhesive_bottle_flip_cap` | grasp |
| `flip_cap_adhesive_bottle_bottle_volume` | `flip_cap_adhesive_bottle_body` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model the adhesive, squeeze deformation, the cap snap or curing.
