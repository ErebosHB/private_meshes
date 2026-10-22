# Robot Tote with Bulb Rail

Stackable small-load tote with a moulded bulb rail across the top that a parallel gripper holds from above.

Original concept model by Vanessa Hassouna, developed for AICOR Solutions.
Typology drawn from a public product reference; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint; the rail runs along Y.
Use a unique URDF parser prefix for each instance.
Collision uses one box per wall and the floor, and a cylinder plus boxes for the rail, so the tote stays open from above.
Mass 0.708 kg: the 0.57 kg tare of a 300 x 200 mm small-load carrier plus the rail volume in polypropylene; inertia is approximated from the collision primitives. These are approximate model parameters, not manufacturer specifications.

## Moving parts

The body is a single rigid link; the object has no moving parts, so the rest and inspection renders are the same.

| Joint | Motion | Inspection position |
| --- | --- | --- |
| none | - | - |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `robot_tote_bulb_rail_rail_grip` | `robot_tote_bulb_rail_body` | grasp |
| `robot_tote_bulb_rail_tote_volume` | `robot_tote_bulb_rail_body` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model stacking loads, the stiffness of the ribbed walls or label and lid accessories.
