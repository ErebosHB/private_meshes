import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from link_legacy_paths import LEGACY_PATHS, create_links
from validate_resources import validate


class ResourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for relative in LEGACY_PATHS.values():
            (self.root / relative).mkdir(parents=True, exist_ok=True)
        self.device = self.root / 'objects/laboratory/centrifuge'
        (self.device / 'assets').mkdir()
        (self.device / 'assets/body.glb').write_bytes(b'fixture')
        (self.device / 'model.urdf').write_text('<robot name="test"><link name="body"><visual><geometry><mesh filename="assets/body.glb"/></geometry></visual></link></robot>')
        self.environment = self.root / 'environments/aicor_medical_lab'
        (self.environment / 'environment.urdf').write_text('<robot name="lab"/>')
        (self.environment / 'trajectory.json').write_text('[]')
        (self.environment / 'scene.json').write_text(json.dumps({
            'models': [{'urdf': 'environment.urdf'}], 'trajectory': 'trajectory.json'
        }))

    def test_object_and_environment_references_survive_layout(self):
        result = validate(self.root)
        self.assertEqual(result, {'urdfs': 2, 'json_files': 2, 'references': 3})

    def test_missing_scene_reference_is_reported(self):
        (self.environment / 'trajectory.json').unlink()
        with self.assertRaisesRegex(ValueError, 'Missing resource.*trajectory.json'):
            validate(self.root)

    def test_missing_device_mesh_is_reported(self):
        (self.device / 'assets/body.glb').unlink()
        with self.assertRaisesRegex(ValueError, 'Missing resource.*assets/body.glb'):
            validate(self.root)

    def test_escaping_scene_reference_is_rejected(self):
        (self.environment / 'scene.json').write_text('{"trajectory": "../../outside.json"}')
        with self.assertRaisesRegex(ValueError, 'Unsafe relative path'):
            validate(self.root)

    def test_aliases_resolve_old_paths_and_are_idempotent(self):
        try:
            create_links(self.root)
        except OSError as error:
            if getattr(error, 'winerror', None) == 1314:
                self.skipTest('Windows account cannot create symlinks')
            raise
        create_links(self.root)
        for old, new in LEGACY_PATHS.items():
            self.assertEqual((self.root / old).resolve(), self.root / new)
            self.assertFalse((self.root / old).readlink().is_absolute())
        self.assertEqual((self.root / 'laboratory_devices/centrifuge/model.urdf').read_bytes(),
                         (self.device / 'model.urdf').read_bytes())
        # Local aliases never create duplicate validation entries.
        self.assertEqual(validate(self.root)['urdfs'], 2)

    def test_alias_conflict_does_not_overwrite_or_partially_create(self):
        conflict = self.root / 'aicor_medical_lab'
        conflict.mkdir()
        (conflict / 'local-data.txt').write_text('keep')
        with self.assertRaises(FileExistsError):
            create_links(self.root)
        self.assertEqual((conflict / 'local-data.txt').read_text(), 'keep')
        self.assertFalse((self.root / 'objects_individually').exists())


if __name__ == '__main__':
    unittest.main()
