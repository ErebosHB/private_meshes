# Environments

Assembled scenes live here. An environment combines room geometry, equipment,
initial placements, scene metadata and any runtime assets needed to load it.

| Environment | Scene description | Geometry and articulation |
| --- | --- | --- |
| [AICOR medical laboratory](aicor_medical_lab/README.md) | [`scene.json`](aicor_medical_lab/scene.json) | [`environment.urdf`](aicor_medical_lab/environment.urdf) |

The medical laboratory also contains independently movable sample vessels and
a stopper. Their URDFs and meshes remain in the self-contained scene bundle so
its relative references and runtime behaviour stay intact. Portable exports of
the five instruments are in [objects/laboratory/](../objects/laboratory/README.md).

Copy the complete environment directory, including its notices, when moving a
scene to another project. The PR2 robot and the CRAM/CRAMERA application are
separate dependencies.
