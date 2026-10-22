# Objects

Independently loadable models live here. Copy the complete model folder,
including its meshes, documentation and notices.

| Collection | Contents | Entry point |
| --- | --- | --- |
| [Articulated objects](articulated/README.md) | 157 furniture, appliance, workshop and storage models, grouped into 11 categories | `<category>/<id>-<slug>/model.urdf` or `model.blend` |
| [Laboratory devices](laboratory/README.md) | Centrifuge, dual dispenser, refrigerator, scale and tube rack | `<device>/model.urdf` |

The [web catalogue](https://sunava.github.io/private_meshes/) currently covers the
articulated collection. Laboratory devices are portable URDF exports with their
own metadata; they do not include Blender projects or rendered preview pairs.

The centrifuge's simulation manuals are stored with that device in
[`laboratory/centrifuge/manuals/`](laboratory/centrifuge/manuals/).

Whole rooms and prearranged scenes belong in [environments/](../environments/README.md).
Keep asset-specific licence notices with each model; see the repository's
[licence scope](../NOTICE.md).
