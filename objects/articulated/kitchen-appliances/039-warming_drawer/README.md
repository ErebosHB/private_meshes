# Warming Drawer

Built-in warming drawer with a full-extension drawer, a glass front and a push button on its top lip.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing panel and per drawer wall, so the drawer tray stays open.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; glass 2,500; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `warming_drawer_drawer_joint` | prismatic | 0.309 |
| `warming_drawer_power_button_joint` | prismatic | 0.002 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `warming_drawer_power_button_contact` | `warming_drawer_power_button` | control |
| `warming_drawer_drawer_grip` | `warming_drawer_drawer` | grasp |
| `warming_drawer_drawer_volume` | `warming_drawer_drawer` | container_volume |
| `warming_drawer_drawer_base_surface` | `warming_drawer_drawer` | place_surface |

The URDF supplies geometry, articulation and frames. It does not model heating, the push-to-open latch, the runners' damping or load ratings.
