# Building Dehumidifier

Upright condensation dehumidifier on castors, with a pull-out water tank, fold-up carry handle and control knob.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per cabinet wall and tank wall, so the tank bay and the tank stay open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `dehumidifier_castor_1_joint` | continuous | 0 |
| `dehumidifier_castor_2_joint` | continuous | 0 |
| `dehumidifier_castor_3_joint` | continuous | 0 |
| `dehumidifier_castor_4_joint` | continuous | 0 |
| `dehumidifier_water_tank_joint` | prismatic | 0.17 |
| `dehumidifier_carry_handle_joint` | revolute | 1.35 |
| `dehumidifier_control_knob_joint` | revolute | 2.4 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `dehumidifier_carry_handle_grip` | `dehumidifier_carry_handle` | grasp |
| `dehumidifier_tank_handle_grip` | `dehumidifier_water_tank` | grasp |
| `dehumidifier_tank_volume` | `dehumidifier_water_tank` | container_volume |
| `dehumidifier_control_knob_contact` | `dehumidifier_control_knob` | control |
| `dehumidifier_top_surface` | `dehumidifier_body` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model the refrigerant circuit, airflow, the humidistat, defrost cycles, the tank-full switch or water.
