# Two-Slot Toaster

Two-slot toaster with a carriage lever that lowers the bread racks, a browning dial and a pull-out crumb tray.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one box per housing wall, top strip and slot wall, so both slots stay open from above.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; rubber 1,100; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `toaster_browning_dial_joint` | revolute | 1.57 |
| `toaster_carriage_lever_joint` | prismatic | 0.085 |
| `toaster_crumb_tray_joint` | prismatic | 0.085 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `toaster_browning_dial_contact` | `toaster_browning_dial` | control |
| `toaster_carriage_lever_contact` | `toaster_carriage_lever` | control |
| `toaster_crumb_tray_grip` | `toaster_crumb_tray` | grasp |
| `toaster_front_slot_volume` | `toaster_body` | container_volume |
| `toaster_rear_slot_volume` | `toaster_body` | container_volume |
| `toaster_carry_grip` | `toaster_body` | grasp |

The URDF supplies geometry, articulation and frames. It does not model heating elements, the carriage latch and spring, timing or crumb collection.
