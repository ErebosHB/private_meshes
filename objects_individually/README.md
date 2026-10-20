# Objects, Individually
Each object folder is self-contained: `model.blend` opens in Blender 4.0 or newer (timeline: closed at frame 1, inspection pose at frame 60, closed again at frame 120), and `model.urdf` loads on its own using only the local `assets/*.glb` meshes. Coordinates are metres, Z up, front toward negative Y. Masses and inertias are approximations.

These are original concept models in common product typologies, not replicas of any manufacturer's product.

## Categories

| | Category | Contents | Objects |
| --- | --- | --- | --- |
| <img src="./storage-shelving/001-cube_shelf_drawer_insert/renders/rest.webp" width="120"> | **[Storage & Shelving](./storage-shelving/)** | Shelves, cabinets, chests, sideboards, display and filing cabinets. | 25 |
| <img src="./wardrobes/004-wardrobe_frame_hinged_doors/renders/rest.webp" width="120"> | **[Wardrobes](./wardrobes/)** | Full-height wardrobes with hinged or sliding doors, rails and baskets. | 3 |
| <img src="./seating/016-swivel_office_chair/renders/rest.webp" width="120"> | **[Seating](./seating/)** | Chairs, stools and armchairs with lifts, swivels and reclining backs. | 3 |
| <img src="./tables-desks/017-sit_stand_desk/renders/rest.webp" width="120"> | **[Tables & Desks](./tables-desks/)** | Desks and tables with height adjustment, drawers, cable flaps and tilting tops. | 5 |
| <img src="./room-dividers/020-folding_partition_screen/renders/rest.webp" width="120"> | **[Room Dividers](./room-dividers/)** | Folding screens and partitions that stand free. | 1 |
| <img src="./kitchen-appliances/031-washing_machine/renders/rest.webp" width="120"> | **[Kitchen & Appliances](./kitchen-appliances/)** | Kitchen runs, corner kitchens, islands, cabinets and bins, plus laundry, dishwashing, cooling, cooking and countertop appliances. | 48 |
| <img src="./tools-workshop/046-wet_dry_vacuum/renders/rest.webp" width="120"> | **[Tools & Workshop](./tools-workshop/)** | Power tools and workshop machines: drills, saws, grinders, vacuums, compressors and pumps, plus welding, soldering, joining and adhesive equipment. | 54 |
| <img src="./containers-boxes/139-attached_lid_container/renders/rest.webp" width="120"> | **[Containers & Boxes](./containers-boxes/)** | Lidded and folding crates, mesh pallet boxes, drums and walk-in storage containers. | 7 |
| <img src="./material-handling/144-hand_pallet_truck/renders/rest.webp" width="120"> | **[Material Handling](./material-handling/)** | Pallet trucks, tipping skips and other equipment for moving loads around a warehouse. | 3 |
| <img src="./ladders-steps/146-mobile_platform_steps/renders/rest.webp" width="120"> | **[Ladders & Steps](./ladders-steps/)** | Mobile platform steps for reaching upper shelf levels safely. | 1 |
| <img src="./hazardous-storage/147-fire_safety_cabinet/renders/rest.webp" width="120"> | **[Hazardous Materials Storage](./hazardous-storage/)** | Safety and chemical cabinets, sump pallets and depots for flammable or polluting substances. | 4 |

## Layout

```
<category>/
  README.md                 overview with renders
  <id>-<slug>/
    model.blend
    model.urdf
    assets/*.glb            one mesh per link
    README.md               joints and interaction frames
    NOTICE.md
    renders/rest.webp       closed
    renders/open.webp       moving parts open
```

`collection.json` lists every object with its id, category, size, joints, interaction frames and variant links.
