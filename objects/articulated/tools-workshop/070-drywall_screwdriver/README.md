# Drywall Screwdriver

Pistol screwdriver with a sliding depth-locator nose, a swing-out belt clip, direction switch and trigger.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, grip, nose and clip, so the gap behind the belt clip stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `drywall_screwdriver_depth_nose_joint` | prismatic | 0.012 |
| `drywall_screwdriver_belt_clip_joint` | revolute | -1.35 |
| `drywall_screwdriver_direction_switch_joint` | prismatic | 0.008 |
| `drywall_screwdriver_trigger_joint` | prismatic | 0.008 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `drywall_screwdriver_pistol_grip` | `drywall_screwdriver_body` | grasp |
| `drywall_screwdriver_belt_clip_hook` | `drywall_screwdriver_belt_clip` | wall_mount |
| `drywall_screwdriver_trigger_contact` | `drywall_screwdriver_trigger` | control |
| `drywall_screwdriver_direction_switch_contact` | `drywall_screwdriver_direction_switch` | control |
| `drywall_screwdriver_nose_face` | `drywall_screwdriver_depth_nose` | tool_attachment |

The URDF supplies geometry, articulation and frames. It does not model the screw clutch, depth-stop clutch release, motor speed, screw feeding or bit retention.
