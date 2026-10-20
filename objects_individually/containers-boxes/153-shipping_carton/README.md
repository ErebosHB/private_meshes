# Shipping Carton with Top Flaps

Small single-wall regular slotted carton whose four top flaps hinge on the top edges and fold over the opening.

Original AICOR concept model. Principal author and design direction: Vanessa Hassouna.
Typology drawn from a public product reference; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Copy this entire folder, including its notices, for an authorized reuse.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per wall, the bottom and each flap, so the carton stays open from above.
Masses/inertias are approximate model parameters (about 90 g of board), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `shipping_carton_front_flap_joint` | revolute | 1.20 |
| `shipping_carton_back_flap_joint` | revolute | 1.20 |
| `shipping_carton_left_flap_joint` | revolute | 1.20 |
| `shipping_carton_right_flap_joint` | revolute | 1.20 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `shipping_carton_carton_volume` | `shipping_carton_body` | container_volume |
| `shipping_carton_front_flap_grip` | `shipping_carton_front_flap` | grasp |
| `shipping_carton_back_flap_grip` | `shipping_carton_back_flap` | grasp |
| `shipping_carton_left_flap_grip` | `shipping_carton_left_flap` | grasp |
| `shipping_carton_right_flap_grip` | `shipping_carton_right_flap` | grasp |

The URDF supplies geometry, articulation and frames. It does not model board bending, creases, glue or tape, or the flap order needed to close it.
