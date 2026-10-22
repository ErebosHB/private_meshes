# Contact Grill

Countertop contact grill with a hinged upper plate, ribbed cooking plates and a temperature dial.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing shell and cooking plate, so the gap between the plates stays open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; glass 2,500; rubber 1,100; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `contact_grill_temperature_dial_joint` | revolute | 1.57 |
| `contact_grill_upper_plate_joint` | revolute | 1.2 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `contact_grill_temperature_dial_contact` | `contact_grill_temperature_dial` | control |
| `contact_grill_upper_plate_grip` | `contact_grill_upper_plate` | grasp |
| `contact_grill_lower_plate_surface` | `contact_grill_body` | place_surface |
| `contact_grill_carry_grip` | `contact_grill_body` | grasp |

The URDF supplies geometry, articulation and frames. It does not model heating, the floating-hinge height adjustment, fat run-off or load ratings.
