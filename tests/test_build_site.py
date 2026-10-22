import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

SPEC = importlib.util.spec_from_file_location('build_site', Path(__file__).resolve().parents[1] / 'scripts/build_site.py')
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class CatalogueBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'objects' / 'articulated'
        self.folder = self.source / 'storage/001-test'
        for name in ('model.blend', 'README.md', 'NOTICE.md', 'assets/body.glb',
                     'renders/rest.webp', 'renders/open.webp'):
            file = self.folder / name
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_bytes(b'fixture')
        (self.folder / 'model.urdf').write_text('<robot name="test"><link name="body"><visual><geometry><mesh filename="assets/body.glb"/></geometry></visual></link></robot>')
        self.data = {'categories': [{'key': 'storage', 'title': 'Storage', 'count': 99}],
                     'objects': [{'id': '001', 'folder': 'storage/001-test', 'category': 'storage', 'joints': [{}], 'frames': [{}, {}]}]}
        self.save()
        (self.root / 'site').mkdir()
        for name in ('index.html', 'styles.css', 'app.js'):
            (self.root / 'site' / name).write_text('fixture')
        (self.root / 'NOTICE.md').write_text('Repository licence scope')
        (self.root / 'LICENSE.txt').write_text('Repository licence')

    def save(self):
        (self.source / 'collection.json').write_text(json.dumps(self.data))

    def test_build_packages_complete_relative_meshes_and_notices(self):
        stats = builder.build(self.root)
        self.assertEqual(stats, {'objects': 1, 'categories': 1, 'joints': 1, 'frames': 2})
        data = json.loads((self.root / 'dist/catalogue.json').read_text())
        self.assertEqual(data['categories'][0]['count'], 1)
        with ZipFile(self.root / 'dist' / data['objects'][0]['download']) as archive:
            self.assertIsNone(archive.testzip())
            for name in ('model.blend', 'model.urdf', 'assets/body.glb', 'NOTICE.md', '_repository/NOTICE.md'):
                self.assertIn('001-test/' + name, archive.namelist())
        self.assertTrue((self.root / 'dist/models/storage/001-test/renders/rest.webp').is_file())

    def test_missing_asset_fails_before_replacing_good_build(self):
        builder.build(self.root)
        previous = (self.root / 'dist/catalogue.json').read_bytes()
        (self.folder / 'assets/body.glb').unlink()
        with self.assertRaisesRegex(ValueError, 'Missing mesh'):
            builder.build(self.root)
        self.assertEqual((self.root / 'dist/catalogue.json').read_bytes(), previous)

    def test_unlisted_new_model_fails_with_clear_error(self):
        extra = self.source / 'storage/002-unlisted/model.urdf'
        extra.parent.mkdir()
        extra.write_text('<robot/>')
        with self.assertRaisesRegex(ValueError, 'Catalogue/folder mismatch'):
            builder.read_catalogue(self.root)

    def test_unsafe_paths_and_symlinks_rejected(self):
        for value in ('../outside', '/etc/passwd', 'storage/../../outside', 'storage\\file'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                builder.local_path(self.source, value)
        (self.folder / 'linked').symlink_to(self.root / 'NOTICE.md')
        with self.assertRaises(ValueError):
            builder.read_catalogue(self.root)

    def test_duplicate_ids_rejected(self):
        self.data['objects'].append(copy.deepcopy(self.data['objects'][0]))
        self.save()
        with self.assertRaisesRegex(ValueError, 'Duplicate object'):
            builder.read_catalogue(self.root)

    def test_missing_preview_and_unknown_category_rejected(self):
        (self.folder / 'renders/open.webp').unlink()
        with self.assertRaisesRegex(ValueError, 'Missing .*renders/open.webp'):
            builder.read_catalogue(self.root)
        self.data['objects'][0]['category'] = 'unknown'
        self.save()
        with self.assertRaisesRegex(ValueError, 'Unknown category'):
            builder.read_catalogue(self.root)

    def test_rebuild_removes_stale_downloads(self):
        builder.build(self.root)
        stale = self.root / 'dist/downloads/deleted-object.zip'
        stale.touch()
        builder.build(self.root)
        self.assertFalse(stale.exists())


if __name__ == '__main__':
    unittest.main()
