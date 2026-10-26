# private_meshes: credits and licence

- **Author and design direction:** Vanessa Hassouna (33067562+sunava@users.noreply.github.com)
- **Developed for:** AICOR Solutions
- **Copyright:** Copyright (c) 2026, Vanessa Hassouna; Copyright (c) 2026, Yannick Schröder, each for
  the parts listed under their name below
- **Licence:** BSD 3-Clause License, see [LICENSE.txt](LICENSE.txt) (SPDX: `BSD-3-Clause`), for the content
  listed under "Covered" and "Contribution by Yannick Schröder"

## Covered: Copyright (c) 2026, Vanessa Hassouna

- `environments/aicor_medical_lab/` and `objects/laboratory/` (including the centrifuge manuals): the AICOR laboratory
  assets and the manuals of the simulated centrifuge.
- `objects/articulated/`: objects #151 and later, and the entries and rows that describe
  them in `collection.json` and the catalogue READMEs.
- The repository's top-level `README.md`, `NOTICE.md` and `rights.json`.

## Contribution by Yannick Schröder: Copyright (c) 2026, Yannick Schröder

Licensed under the BSD 3-Clause License, see [LICENSE.txt](LICENSE.txt) (SPDX: `BSD-3-Clause`):

- Objects #001-#150 in `objects/articulated/`, together with `PROMPT.md`, `collection.json`,
  `objects/articulated/README.md` and the category `README.md` files in the form he added
  them (commit c9cb1b3, pull request #1, 2026-10-19). Each of these object folders carries
  its own `LICENSE.txt` and names him in its `NOTICE.md` and `README.md`.
- The semantic annotations: `scripts/annotate_semantics.py`, `scripts/annotation_graph.html`,
  `scripts/sync_semantics.py`, `tests/test_annotate_semantics.py`, `tests/test_sync_semantics.py`,
  `objects/articulated/semantic_concepts.json`, the `semantics.json` file in every object folder, the
  `group` of each category in `collection.json` and the "Semantic annotations" section of
  `objects/articulated/README.md`. A `semantics.json` describes the model in its folder;
  the model itself stays with the copyright holder named in that folder's `NOTICE.md`.

## Not covered

Not covered by the licence, and keeping their own rights and terms: the AICOR name and the
AICOR logo artwork in the visual models (no trademark or logo permission is granted), font
artwork, the separately obtained PR2 model, and the CRAM/CRAMERA software. Typology references named in object notices (manufacturer or retailer catalogues)
were used only for the kind of object and its size class; no material from them is included.

## History

Licence history: the laboratory assets were first described as GPL-3.0-only, then from
2026-09-25 as permission-only (`LicenseRef-AICOR-Laboratory-Assets`). On 2026-10-21 the
copyright holder relicensed them under BSD-3-Clause. Permissions validly granted earlier are
not withdrawn.

Objects #001-#150 and the files contributed with them were unlicensed ("licence pending")
from 2026-10-19 until 2026-10-22, when Yannick Schröder licensed them under BSD-3-Clause.
