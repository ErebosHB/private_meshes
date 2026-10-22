# Hot-Melt Glue Gun

Pistol glue gun with a feed trigger, a glue stick in the rear inlet and a fold-down wire stand.

Original concept model by Yannick Schröder.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Licensed under BSD-3-Clause (see LICENSE.txt and NOTICE.md); keep both with every copy.

Coordinates are metres, Z up, front toward negative Y. Origin at floor level, centre of the footprint.
Use a unique URDF parser prefix for each instance.
Collision uses one primitive per housing block, nozzle and wire segment, so the gap under the barrel stays open.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `hot_melt_glue_gun_feed_trigger_joint` | revolute | 0.32 |
| `hot_melt_glue_gun_stand_joint` | revolute | 1.38 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `hot_melt_glue_gun_handle_grip` | `hot_melt_glue_gun_body` | grasp |
| `hot_melt_glue_gun_feed_trigger_contact` | `hot_melt_glue_gun_feed_trigger` | control |
| `hot_melt_glue_gun_nozzle_tip` | `hot_melt_glue_gun_body` | tool_attachment |
| `hot_melt_glue_gun_stand_foot_grip` | `hot_melt_glue_gun_stand` | grasp |

The URDF supplies geometry, articulation and frames. It does not model melt temperature, glue flow, the feed clamp, drip behaviour or burn hazards.
