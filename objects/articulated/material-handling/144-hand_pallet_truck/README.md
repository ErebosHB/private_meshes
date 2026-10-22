# Hand Pallet Truck

Manual pallet truck: pumping the drawbar lifts the forks, a lever on the handle releases them, and steering wheels and load rollers roll.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per fork channel wall and cross plate, and one cylinder per wheel, roller, pump column and handle tube.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (steel 7,850; ABS/HDPE 1,050; rubber 1,200 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `hand_pallet_truck_forks_joint` | prismatic | 0.11 |
| `hand_pallet_truck_drawbar_joint` | revolute | 1 |
| `hand_pallet_truck_release_lever_joint` | revolute | 0.45 |
| `hand_pallet_truck_left_steer_wheel_joint` | continuous | 0 |
| `hand_pallet_truck_right_steer_wheel_joint` | continuous | 0 |
| `hand_pallet_truck_left_load_roller_joint` | continuous | 0 |
| `hand_pallet_truck_right_load_roller_joint` | continuous | 0 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `hand_pallet_truck_tether_anchor` | `hand_pallet_truck_body` | wall_mount |
| `hand_pallet_truck_fork_surface` | `hand_pallet_truck_forks` | place_surface |
| `hand_pallet_truck_handle_grip` | `hand_pallet_truck_drawbar` | grasp |
| `hand_pallet_truck_release_lever_tip` | `hand_pallet_truck_release_lever` | control |

The URDF supplies geometry, articulation and frames. It does not model the hydraulic pump and valve, steering rotation of the wheel unit, the load-roller linkage, braking or load ratings.
