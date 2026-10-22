# Portable Electrode Oven

Cylindrical holding oven for welding electrodes with a hinged lid and a bail handle that swings up over the top.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes around the shell wall and a disc for the chamber floor, so the electrode chamber stays open under the lid.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `electrode_drying_oven_lid_joint` | revolute | 1.2 |
| `electrode_drying_oven_bail_handle_joint` | revolute | 2.38 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `electrode_drying_oven_bail_handle_grip` | `electrode_drying_oven_bail_handle` | grasp |
| `electrode_drying_oven_lid_tab_grip` | `electrode_drying_oven_lid` | grasp |
| `electrode_drying_oven_chamber_volume` | `electrode_drying_oven_body` | container_volume |

The URDF supplies geometry, articulation and frames. It does not model the heater, thermostat, insulation, lid seal or the electrodes as separate parts.
