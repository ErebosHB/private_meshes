# Object catalogue

The static catalogue is generated from `objects/articulated/collection.json` and
the object folders. It includes category filters, full-text search, sorting,
rest/inspection previews, joint limits, interaction frames, each object's semantic
annotations (read from its `semantics.json`) and complete ZIP downloads. There is no server, package installation, external CDN or Blender
rendering step. All URLs are relative, including downloads and object deep links,
so the site works under the GitHub Pages repository path.

## Enable automatic publication

1. Merge the catalogue files and `.github/workflows/pages.yml` into `main`.
2. In the repository, open **Settings → Pages → Build and deployment → Source**
   and choose **GitHub Actions**. This requires a repository administrator.
3. Open **Actions → Build and deploy object catalogue → Run workflow** and select
   `main`. This retries publication if the first push ran before Pages was enabled.

Site address: [Objects, Individually](https://sunava.github.io/private_meshes/).
The catalogue becomes available there after the deployment job succeeds.
Subsequent pushes to `main` that change models, catalogue source, build code,
tests, workflow or notices rebuild and publish automatically. Pull requests run
tests and build the entire site without deploying. A manual run on another branch
builds only. No personal access token or repository secret is required by the workflow.

## Local preview

Requires Python 3.10+ (and Node.js only for the optional JavaScript syntax check).
From the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_resources.py
node --check site/app.js
python3 scripts/build_site.py
python3 -m http.server 8000 --directory dist
```

Open `http://localhost:8000`. Serve the build over HTTP; opening `index.html` as a
local file will prevent browsers from fetching its catalogue. `dist/` is generated
and ignored by Git. The builder recreates it on each successful validation.

## Adding and updating objects

Keep the object's entry in `objects/articulated/collection.json` aligned with its
folder. Every model needs `model.blend`, `model.urdf`, local mesh references,
`README.md`, `NOTICE.md`, and `renders/rest.webp` plus `renders/open.webp`. Add new
category metadata to the same manifest when needed. Counts are computed from the
object entries on every build. Regenerate and commit previews when a model changes;
this workflow does not render Blender files.

The build rejects missing previews, missing meshes, unknown categories, duplicate
IDs/folders, symlinks, paths escaping the collection, and model folders absent from
the manifest. Failures stop deployment and leave the published site untouched.
Downloads contain the complete object folder and its original notices, plus the
repository licence and scope notice under `_repository/`. The catalogue does not
assign a new licence to models whose licence is pending.

The workflow uses GitHub-hosted Ubuntu runners and the standard Pages actions.
Its build job has only read permission; only the deployment job can publish Pages.
Changes in both `objects/` and `environments/` trigger validation. All URDF mesh
references and scene JSON file references are checked before the site is built.
The web catalogue itself continues to use `objects/articulated/`; the repository
also contains portable laboratory devices under `objects/laboratory/`.
