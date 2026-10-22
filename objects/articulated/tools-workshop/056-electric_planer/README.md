# Electric Planer

Hand planer with a closed rear handle, a front depth knob, a chip chute that swivels left or right and a cutter drum.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per sole, housing block and handle bar, so the opening inside the rear handle stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `electric_planer_cutter_drum_joint` | continuous | 0.8 |
| `electric_planer_depth_knob_joint` | revolute | 3 |
| `electric_planer_chip_chute_joint` | revolute | 3.14 |
| `electric_planer_trigger_joint` | prismatic | 0.008 |
| `electric_planer_lock_off_button_joint` | prismatic | 0.004 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `electric_planer_rear_grip` | `electric_planer_body` | grasp |
| `electric_planer_depth_knob_grip` | `electric_planer_depth_knob` | grasp |
| `electric_planer_trigger_contact` | `electric_planer_trigger` | control |
| `electric_planer_lock_off_contact` | `electric_planer_lock_off_button` | control |
| `electric_planer_chute_outlet` | `electric_planer_chip_chute` | tool_attachment |
| `electric_planer_cutter_edge` | `electric_planer_cutter_drum` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model cutting depth stops, blade sharpness, the drive belt, rebating, chip extraction airflow or kickback.
