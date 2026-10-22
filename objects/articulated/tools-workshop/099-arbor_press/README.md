# Manual Arbor Press

Bench press for pressing bearings and pins: pulling the lever drives the rack ram down onto an indexable anvil plate.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per base, column, head, ram, lever and anvil part, so the pressing gap stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `arbor_press_anvil_plate_joint` | revolute | 1.57 |
| `arbor_press_ram_joint` | prismatic | 0.11 |
| `arbor_press_lever_joint` | revolute | 1 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `arbor_press_lever_knob_grip` | `arbor_press_lever` | grasp |
| `arbor_press_ram_tip` | `arbor_press_ram` | tool_attachment |
| `arbor_press_anvil_surface` | `arbor_press_anvil_plate` | place_surface |
| `arbor_press_rear_anchor` | `arbor_press_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model the rack-and-pinion coupling, press force, mechanical advantage or bench mounting.
