# Mobile Tray Rack

Stainless mobile rack with runners for baking or confectionery trays on four castors; trays slide out to the front.

Original AICOR concept model. Principal author and design direction: Vanessa Hassouna.
Typology drawn from a public product reference; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Copy this entire folder, including its notices, for an authorized reuse.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint; trays slide out toward negative Y.
Use a unique URDF parser prefix for each instance.
Collision uses boxes for the posts, the top frame and every tray, and cylinders for the castors, so the tray slots stay open.
Masses/inertias are approximate model parameters (stainless tube and sheet), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `mobile_tray_rack_tray_joint` | prismatic | 0.38 |
| `mobile_tray_rack_castor_0_joint` | continuous | 0.00 |
| `mobile_tray_rack_castor_1_joint` | continuous | 0.00 |
| `mobile_tray_rack_castor_2_joint` | continuous | 0.00 |
| `mobile_tray_rack_castor_3_joint` | continuous | 0.00 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `mobile_tray_rack_tray_surface` | `mobile_tray_rack_tray` | place_surface |
| `mobile_tray_rack_tray_grip` | `mobile_tray_rack_tray` | grasp |
| `mobile_tray_rack_push_grip` | `mobile_tray_rack_body` | grasp |
| `mobile_tray_rack_wall_anchor` | `mobile_tray_rack_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model castor swivel or brakes, the trays' load rating or any food on the trays.
