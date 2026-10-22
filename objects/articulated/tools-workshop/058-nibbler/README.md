# Nibbler

Stick-body sheet-metal nibbler lying on its side, with a die head that indexes around the body axis, a punch and a slide switch.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per body section and jaw part, so the cutting gap between punch and die stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `nibbler_die_head_joint` | revolute | 1.57 |
| `nibbler_punch_joint` | prismatic | 0.005 |
| `nibbler_slide_switch_joint` | prismatic | 0.012 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `nibbler_body_grip` | `nibbler_body` | grasp |
| `nibbler_slide_switch_contact` | `nibbler_slide_switch` | control |
| `nibbler_cutting_gap` | `nibbler_die_head` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model punch stroke rate, sheet thickness limits, die wear, chip ejection or vibration.
