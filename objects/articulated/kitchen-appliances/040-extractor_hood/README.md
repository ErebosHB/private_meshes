# Under-Cabinet Extractor Hood

Wall-mounted extractor hood with a pull-out telescopic visor, grease filters and two push buttons.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at the back-bottom edge centre.
Use a unique URDF parser prefix for each instance.
Collision uses boxes per housing panel, filter and visor plate; the housing stays open behind the filters.
Masses/inertias are approximate model parameters from primitive volumes and typical densities (ABS 1,050; aluminium 2,700; glass 2,500; stainless steel 7,850 kg/m³), not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `extractor_hood_visor_joint` | prismatic | 0.16 |
| `extractor_hood_fan_button_joint` | prismatic | 0.003 |
| `extractor_hood_light_button_joint` | prismatic | 0.003 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `extractor_hood_fan_button_contact` | `extractor_hood_fan_button` | control |
| `extractor_hood_light_button_contact` | `extractor_hood_light_button` | control |
| `extractor_hood_visor_grip` | `extractor_hood_visor` | grasp |
| `extractor_hood_wall_anchor` | `extractor_hood_body` | wall_mount |
| `extractor_hood_duct_attachment` | `extractor_hood_body` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the fan, airflow, lighting, grease filtering, the cabinet or wall fixing strength.
