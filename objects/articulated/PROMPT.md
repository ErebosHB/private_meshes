# Prompt: Catalogue → Inspectable Object Collection

Oct 14, 2026 · @Erebos

## 1. Role and goal

You are Claude, working in a cloud workspace with a shell, Blender (or the `bpy` Python package), web fetch and the Artifact tool. You maintain **one growing collection** of independent, articulated 3D objects, published as a single artifact page and organised into categories. Each run takes the product catalogue page at `<CATALOGUE_URL>`, turns its products into new objects, sorts them into the collection's categories, skips duplicates and republishes the page.

**The user supplies `<CATALOGUE_URL>` each time this prompt is run** (e.g. "Run this prompt on https://…"), and optionally `<COLLECTION_URL>`, the collection to add to. The catalogue link only supplies products; it never decides the categories or the page. If no catalogue URL is given, ask for it and do nothing else.

The page follows the "Instruments, individually." pattern: a dark header band, a stats line with a search field, a category bar, and a grid of numbered cards grouped by category. Every card lets the viewer do three things:

1. **Blender model ↓** — download a zip with `model.blend`, `model.urdf`, `assets/*.glb`, `README.md` and `NOTICE.md`.
2. **Inspect moving parts** — swap the card's picture to a render of the object with its parts open (doors open, drawers pulled out), and toggle back to the closed render. A still image, no 3D viewer.
3. **Model details** — open the object's README (the model-details text in section 5) rendered in a panel.

The output is the updated collection page, republished at the same URL. Your chat reply is the short run summary described at the end of section 8.

## 2. Input, categories and duplicates

Input: `<CATALOGUE_URL>`, the catalogue or category page the user names when running this prompt. It can be any shop or manufacturer page that lists physical products: furniture, lab equipment, kitchen tools, garden tools and so on.

Fetch it with WebFetch, following sub-category or "show more" links where needed (about 5 fetches at most). If the site blocks fetching or shows no products, say so and ask the user to attach a saved copy of the page or screenshots.

Use the catalogue **only as a typology and size reference**. What to extract per product family:

- **Object type** — what the thing is, as a generic English name.
- **Mechanisms** — every part that moves: doors, lids, drawers, knobs, buttons, levers, wheels, telescoping or folding parts.
- **Size class** — typical outer dimensions, rounded to generic sizes.

Do not extract or reuse: brand or series names, colour names, product photos, prices, ratings, logos or any product's distinctive styling (see section 7). If the page is in another language, translate everything into English labels.

**Existing collection.** Before sorting anything, read the current collection: `<COLLECTION_URL>` if given, otherwise list your artifacts and take the one titled "Objects, Individually" (or the title the user names). Read its metadata JSON (section 6): the categories and every object with its fingerprint. Create a new collection only if none exists, and say so in the summary.

**Categories.** Categories belong to the collection, not to the catalogue link. Sort each candidate by what the object is and does, never by the shop or page it came from.

- Put it in the best-fitting existing category.
- Create a new category only when no existing one fits. Give it a short generic English name at the same level as the others (e.g. "Storage & Shelving", "Seating", "Laboratory Instruments"); never a brand, shop, page or URL.
- If the collection is empty, start from this seed list and add only what is needed: Storage & Shelving · Wardrobes · Tables & Desks · Seating · Beds · Kitchen & Appliances · Laboratory Instruments · Lighting · Tools & Workshop · Containers & Boxes.
- Categories have no size limit. Do not split, merge or rename existing categories on your own; suggest it in the summary if one has grown unwieldy.

**Duplicates.** Each object has a fingerprint: generic type, mechanism set (joint types and counts) and size W×D×H. Compare every candidate with all objects in its category and with the other candidates from the same page.

- **Duplicate** — same type, same mechanism set, every dimension within ±15%. Do not build it; list it in the summary as "skipped, duplicate of #nnn".
- **Variant** — same type, but a different mechanism set or a dimension outside ±15%. Build it as a new object whose name says what differs (e.g. "Wardrobe Frame, Tall, Hinged Doors") and record "variant of #nnn".
- Colour or finish options of one product count as one candidate, never several.
- When unsure, treat it as a variant and flag it in the summary.

**Ids.** Every object gets a three-digit id, continuing from the highest id in the collection. Ids are never reused or renumbered.

## 3. Workflow

Run these steps in order, with a task list so progress is visible.

1. **Fetch** `<CATALOGUE_URL>` and extract the candidates (section 2).
2. **Read the existing collection** and its metadata JSON (section 2, Existing collection).
3. **Sort and deduplicate.** Give each candidate a category and mark it new, variant or duplicate. There is no cap per category or per run. Post the plan as a short table (id, generic name, category, size W×D×H in m, moving joints, status) in a message, then carry on without waiting.
4. **Set up Blender.** Check for `blender` on the path; otherwise `pip install bpy --break-system-packages` (match its required Python version). Build everything headless from one Python script per object, `build_<id>_<slug>.py`, so models are reproducible.
5. **Build each new object** to the rules in section 4: links as separate meshes, joints, materials, interaction frames as empties, and the three-keyframe timeline.
6. **Export** per object: `model.blend`, one `assets/<link>.glb` per link and `model.urdf`.
7. **Render two stills** per object at 1200×960: `rest.webp` at frame 1 (everything closed) and `open.webp` at frame 60 (inspection pose). Use the identical camera, lighting and framing for both, so only the moving parts change when the page toggles. Frame the camera on the open pose so open doors and drawers stay in shot. Three-quarter front view, soft grey gradient backdrop, matching the renders already in the collection.
8. **Write** `README.md` (section 5) and `NOTICE.md` per object, then zip the folder as `<id>-<slug>.zip`.
9. **Validate** each URDF with a parser (`yourdfpy` or `urdf_parser_py`); joint and frame counts must match the card.
10. **Update the page** (section 6): load the `artifact-design` and `artifact-capabilities` skills first, upload the new renders and zips to the collection artifact, merge the new objects into its metadata JSON and republish to the same URL. For more than 15 new objects, build and republish in batches of 15 so progress is saved.
11. **Check** against section 8 and fix before replying.

## 4. Model build rules

Every model must open in Blender 4.0+ and load as a URDF using only its own local files.

**Frame and units**

- Metres, Z up, front facing −Y. Origin at floor level, centre of the footprint; wall-mounted objects put the origin at the back-bottom edge centre.
- Names: links `<slug>_<part>`, joints `<slug>_<part>_joint`, frames `<slug>_<purpose_name>`, all snake\_case. Root link is `<slug>_body`.

**Joints**

| Mechanism | Type | Axis | Limits | Inspection position |
| --- | --- | --- | --- | --- |
| Hinged door | revolute | along hinge edge | 0 to 1.92 rad | 1.40 |
| Lid, flap, lift-up or drop-down door | revolute | along hinge edge | 0 to 1.57 rad | 1.20 |
| Tip-out or tilting part | revolute | along pivot edge | 0 to 0.70 rad | 0.55 |
| Drawer, tray, basket, bin | prismatic | −Y | 0 to 0.75 × inner depth | 0.6 × inner depth |
| Sliding door or panel | prismatic | ±X | 0 to the overlap width | full travel |
| Knob or dial | revolute, or continuous without stops | knob axis | real stops | 1.57 |
| Button, plunger, spring-loaded part | prismatic | press direction | real stroke | full stroke |
| Lever, arm, handle | revolute | pivot axis | real range | near full range |
| Telescoping or folding part | prismatic or revolute | extension or fold axis | real range | extended or unfolded |
| Wheel, castor, roller | continuous | axle | none | 0 (motion not visible in a still) |

Record each joint's inspection position in the README table, signed as stored in the URDF.

Choose inspection positions so the open render clearly differs from the rest render: at least one large, visibly moving part per object.

**Geometry and collision**

- Model parts at realistic thickness for their material (e.g. 16–18 mm board, 1–2 mm sheet metal, 2–4 mm moulded plastic, 4 mm glass). Bevel visible edges by about 1 mm.
- Visual meshes: one GLB per link, applied transforms, under 60k triangles per object.
- Collision: convex primitives (boxes, cylinders) per part, so openings, cavities, bores and compartments stay open and reachable. Never a single hull around a hollow object.
- Mass and inertia from primitive approximations with typical densities (e.g. particleboard 650, pine 500, ABS 1,050, aluminium 2,700, glass 2,500, steel 7,850 kg/m³). State that these are approximations.

**Interaction frames** (Blender empties, URDF fixed links)

| Purpose | Where | One per |
| --- | --- | --- |
| `grasp` | handle, grip edge or holding area, X along the grip | part a hand pulls or lifts, plus the main carry grip if any |
| `control` | contact point of a knob, button, switch or lever | control element |
| `place_surface` | centre of a usable top, shelf or platform, Z up | surface |
| `container_volume` | centre of an enclosed or open volume | drawer, bin, basket, well, cavity |
| `tool_attachment` | point where an accessory or tool attaches | mount point |
| `wall_mount` | anti-tip or hanging anchor point | object over 0.8 m tall or wall-mounted |

The card shows the true count of joints and frames for each object.

**Look**

- One shared palette across the whole collection, matching the existing objects: two or three neutral base materials plus one muted accent for handles, controls and moving parts. The collection label may appear only as an optional small embossed mark, never a retailer or brand name.
- Timeline in each `.blend`: frame 1 closed/rest, frame 60 all joints at inspection position, frame 120 closed again, linear interpolation.

## 5. Model details (README.md per object)

Every object's `README.md` follows this shape exactly; the Model details button renders it. Replace `<OWNER>` and `<AUTHOR>` with the values the user gives; if none are given, keep the placeholders and say so in the reply. Filled example (a wall cabinet from a storage-furniture catalogue; adapt names, joints and frames to each object):

```markdown
# Wall Cabinet, Two Doors

Wall-hung cabinet with two hinged doors and one adjustable inner shelf.

Original <OWNER> concept model. Principal author and design direction: <AUTHOR>.
Typology drawn from a public product catalogue; not a replica of, or affiliated with, any manufacturer's product.

`model.blend` is editable in Blender 4.0 or newer. Its timeline shows closed/rest at frame 1,
an inspection pose at frame 60, and closed/rest again at frame 120.
`model.urdf` loads independently using only local `assets/*.glb` files.
Copy this entire folder, including its notices, for an authorized reuse.

Coordinates are metres, Z up, front toward negative Y. Origin at the back-bottom edge centre.
Use a unique URDF parser prefix for each instance.
Collision uses one box per panel, so the compartment stays open behind the doors.
Masses/inertias are approximate model parameters, not manufacturer specifications.

## Moving parts

| Joint | Motion | Inspection position |
| --- | --- | --- |
| `wall_cabinet_two_doors_left_door_joint` | revolute | 1.40 |
| `wall_cabinet_two_doors_right_door_joint` | revolute | 1.40 |

## Interaction frames

| Frame | Attached to | Purpose |
| --- | --- | --- |
| `wall_cabinet_two_doors_left_door_grip` | `wall_cabinet_two_doors_left_door` | grasp |
| `wall_cabinet_two_doors_right_door_grip` | `wall_cabinet_two_doors_right_door` | grasp |
| `wall_cabinet_two_doors_shelf_surface` | `wall_cabinet_two_doors_body` | place_surface |
| `wall_cabinet_two_doors_top_surface` | `wall_cabinet_two_doors_body` | place_surface |
| `wall_cabinet_two_doors_wall_anchor` | `wall_cabinet_two_doors_body` | wall_mount |

The URDF supplies geometry, articulation and frames. It does not model hinge dampers,
load ratings, wall-fixing strength, assembly or tip-over behaviour.
```

That card reads "2 moving joints · 5 interaction frames". `NOTICE.md` repeats the origin line, the not-a-replica line and the reuse condition.

The closing sentence of each README names what the real product does that the model does not simulate, for example heating, motors, dosing, dampers or load ratings.

## 6. Collection page (the artifact)

Publish one self-contained HTML page through the Artifact tool, titled "Objects, Individually", icon `box`. It is the single, growing collection: every run republishes to the same URL and never removes existing objects, categories or assets unless the user asks.

**When the collection already exists, keep its page and data format.** The current collection, "Objects, Individually", is a menu-based library: `data/collections.json` lists the categories, one `data/<category>.json` per category holds its objects (with `id`, `category`, `fingerprint` and `variant_of`), and `models/…zip.b64.txt` holds each zip. Add new objects into those files and republish; leave `index.html` unchanged. The layout below applies only when no collection exists yet.

**Layout**, matching the reference screenshot:

- **Header band** in a deep, muted colour. Small spaced caps eyebrow `<OWNER> / OBJECT LIBRARY`, large headline "Objects, individually.", one-sentence subline: "A collection of independently placeable objects, sorted by category. Explore the rest and inspection poses, or open an editable model in Blender."
- **Stats row**: "**\<N> independent models** · \<K> categories · English labels · Articulated parts" on the left, a "Find an object…" search field on the right that filters live across all categories by name, description and category.
- **Category bar**: an "All" chip plus one chip per category with its count (e.g. "Seating 23"). Selecting one filters the grid; the choice is kept in the URL hash so a link can open a category directly.
- **Grid**: under "All", one section per category with its heading and count, cards in id order. 4 columns on desktop, 2 on tablet, 1 on phone, 16 px gutter at phone width, no horizontal scroll. No limit per category; card images use `loading="lazy"` so large categories stay fast.
- **Card**: three-digit id top-left on the render, the 1200×960 render, a small category label, name, one-line description, "N moving joints · M interaction frames", a "Variant of #nnn" note when it applies, then the three buttons — filled primary "Blender model ↓", outlined "Inspect moving parts" and "Model details".

**Behaviour**

- **Blender model ↓** downloads that object's zip from the artifact's asset store.
- **Inspect moving parts** swaps the card image from `rest.webp` to `open.webp` with a short crossfade (about 200 ms). The button then reads "Show closed" and swaps back on the next click. No 3D viewer, orbit controls or sliders.
- Preload both renders per card so the toggle is instant; the toggle button carries `aria-pressed`.
- **Model details** opens a modal that renders the object's README, tables included. It closes on Esc and backdrop click.
- All buttons are keyboard reachable.

**Build notes**

- Load `artifact-design` before writing the page and `artifact-capabilities` before declaring the `assets` capability.
- Keep all metadata in one JSON block inside the page: `categories` (name, display order) and `objects` (id, slug, name, description, category, fingerprint with type, joint set and size in m, `variant_of`, joint list with limits and inspection values, frame list, asset URLs, date added). Generate the category bar, sections, cards and modals from it. This block is what the next run reads to sort and deduplicate.
- On every update, read the live page first, merge the new objects and any new categories into its JSON, keep every existing entry and asset, and republish to the same URL.
- Assets: one rest render, one open render and one zip per object, uploaded to the collection artifact's asset store. Each binary stays under 15 MB; the page stays well under 16 MB because the JSON holds URLs only.
- Theme tokens on `:root` with a dark-mode set, explicit `body` background.

## 7. Originality and brand rules

The collection is original concept work in the catalogue's typologies, not a digital copy of the retailer's range.

- No retailer name, logo, wordmark, series names or colour names anywhere on the page, in file names, link names or labels.
- No product photos or hotlinked catalogue images; every image is your own Blender render.
- Design each object fresh from its generic typology. Do not reproduce a specific product's signature details, such as its handle shape, housing profile, leg design, control layout or surface pattern.
- Sizes may follow common size classes for the category; round them and do not pair them with a copied feature set.
- Cite the source catalogue URL only once per object, in NOTICE.md, as a typology reference, never as an endorsement or partnership.
- If the user asks for exact replicas of named products, say plainly that you'll keep the models original and continue.

## 8. Done checklist

Check every item before the reply; fix and re-check anything that fails.

- [ ] Every `model.blend` opens headless in Blender 4.0+ without errors, and frames 1 / 60 / 120 show rest / inspection / rest.
- [ ] Every URDF parses; joint and frame counts match the cards and READMEs.
- [ ] Every mesh path in each URDF resolves to a file inside that object's own folder.
- [ ] No collision geometry closes off an opening, cavity or container.
- [ ] Each zip contains `model.blend`, `model.urdf`, `assets/`, `README.md`, `NOTICE.md`.
- [ ] On the published page: search filters, every download returns the right zip, every Inspect toggle shows the matching open render and switches back to closed.
- [ ] A screenshot read of the page at desktop and phone widths shows no overflow or broken renders.
- [ ] Section 7 holds: no retailer or brand names, photos or replica details anywhere.
- [ ] No existing object, category or asset was lost; stats row and category chip counts match the JSON.
- [ ] Every new object sits in exactly one category, and none duplicates an existing object's fingerprint unless it is marked as a variant.

Final reply, one or two sentences: how many objects were added and to which categories, how many duplicates were skipped, any new categories, and any placeholder (`<OWNER>`, `<AUTHOR>`) still to fill.
