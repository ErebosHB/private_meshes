# Objects

Independently loadable models live here. Copy the complete model folder,
including its meshes, documentation and notices.

| Collection | Contents | Entry point |
| --- | --- | --- |
| [Articulated objects](articulated/README.md) | 157 furniture, appliance, workshop and storage models, grouped into 11 categories | `<category>/<id>-<slug>/model.urdf` or `model.blend` |
| [Laboratory devices](laboratory/README.md) | Centrifuge, dual dispenser, refrigerator, scale and tube rack | `<device>/model.urdf` |

The [web catalogue](https://sunava.github.io/private_meshes/) covers both
collections, with a Laboratory category and an Articulated/Rigid filter.
The centrifuge and refrigerator have moving joints; the dual dispenser, scale
and tube rack are rigid in their current URDFs. Each device has a rendered
preview and a complete ZIP download. Articulated devices also have an inspection
preview. Laboratory exports include URDF and GLB files, but no Blender project.

The centrifuge's simulation manuals are stored with that device in
[`laboratory/centrifuge/manuals/`](laboratory/centrifuge/manuals/).

Whole rooms and prearranged scenes belong in [environments/](../environments/README.md).
Keep asset-specific licence notices with each model; see the repository's
[licence scope](../NOTICE.md).
