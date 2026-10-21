# Praline Gift Box with Assortment Blister

Sixteen-piece gift box: board base with a thermoformed blister whose cavities are shaped per variety, and a telescope lid.

Original AICOR concept model. Principal author and design direction: Vanessa Hassouna.
Typology drawn from a public product reference; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Copy this entire folder, including its notices, for an authorized reuse.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the box footprint; cavity frames sit at each cavity floor.
Use a unique URDF parser prefix for each instance.
Collision uses boxes for the floor, the four walls and one floor plate per cavity; the lid is a top plate and four walls, so the box stays open from above.
Masses/inertias are approximate model parameters (about 100 g base and blister, 70 g lid), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `praline_gift_box_lid_joint` | prismatic | 0.06 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `praline_gift_box_cavity_0_0_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_0_1_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_0_2_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_0_3_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_1_0_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_1_1_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_1_2_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_1_3_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_2_0_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_2_1_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_2_2_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_2_3_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_3_0_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_3_1_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_3_2_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_cavity_3_3_volume` | `praline_gift_box_body` | container_volume |
| `praline_gift_box_lid_grip` | `praline_gift_box_lid` | grasp |

The URDF supplies geometry, articulation and frames. It does not model board bending, the blister's elasticity, the lid's friction fit or any print.
