import ast
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import sync_semantics as sync

MODULE = '''from semantic_digital_twin.semantic_annotations.mixins import HasRootBody, HasDoors


class Furniture(SemanticAnnotation):
    """Furniture."""


class Dishwasher(HasRootBody, HasDoors):
    """A dishwasher."""


class Chair(Furniture):
    """Abstract class for chairs."""


class OfficeChair(Chair):
    """An office chair."""


class Sofa(Furniture, HasRootBody):
    """A sofa."""
'''
MIXINS = '''class HasRootKinematicStructureEntity(SemanticAnnotation):
    pass


class HasRootBody(HasRootKinematicStructureEntity[Body]):
    pass


class HasDoors(HasRootKinematicStructureEntity):
    pass
'''


def obj(ident, object_type):
    return {'id': ident, 'name': object_type.title(), 'fingerprint': {'type': object_type}}


class FakeCramTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / sync.MODULE_FILE).parent.mkdir(parents=True)
        (self.root / sync.MODULE_FILE).write_text(MODULE)
        (self.root / sync.MODULE_FILE).with_name('mixins.py').write_text(MIXINS)
        self.cram = sync.CramClasses.read(self.root)
        self.registry = {
            'cram': {'repository': 'cram2/x', 'branch': 'main', 'checked': '0' * 40},
            'fallback': 'NaturalLanguageWithTypeDescription',
            'concepts': {
                'Dishwasher': {'cram': 'missing'},
                'Chair': {'cram': 'unusable', 'proposal': {'add_bases': ['HasRootBody']}},
                'OfficeChair': {'cram': 'unusable'},
                'WashingMachine': {'cram': 'missing', 'proposal': {
                    'bases': ['HasRootBody', 'HasDoors'], 'doc': ['A washing machine.'], 'after': 'Dishwasher'}},
            },
            'object_types': {'dishwasher': 'Dishwasher', 'bar stool': 'Chair', 'office chair': 'OfficeChair',
                             'washing machine': 'WashingMachine'},
        }
        self.objects = [obj('001', 'dishwasher'), obj('002', 'bar stool'), obj('003', 'office chair'),
                        obj('004', 'washing machine'), obj('005', 'sofa'), obj('006', 'furniture')]

    def test_status_follows_bases_through_generic_mixins(self):
        self.assertEqual(self.cram.status('Dishwasher'), sync.AVAILABLE)
        self.assertEqual(self.cram.status('Chair'), sync.UNUSABLE)
        self.assertEqual(self.cram.status('WashingMachine'), sync.MISSING)

    def test_compare_finds_one_pull_request_per_difference(self):
        changes = {c.slug: c for c in sync.compare(self.registry, self.cram, self.objects)}
        # 'furniture' matches a cram2 class too, but one without a root body, so it is not offered
        self.assertEqual(set(changes), {'adopt-dishwasher', 'add-bases-chair', 'add-class-washing-machine',
                                        'map-type-sofa'})
        self.assertEqual([o['id'] for o in changes['add-bases-chair'].objects], ['002', '003'])
        self.assertEqual(changes['adopt-dishwasher'].repository, 'private_meshes')
        self.assertEqual(changes['add-class-washing-machine'].repository, 'cram2')

    def test_cram_patches_apply_and_place_classes_after_their_anchor(self):
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        for change in sync.compare(self.registry, self.cram, self.objects):
            if change.repository != 'cram2':
                continue
            patch, warnings = sync.cram_patch(change, self.registry['concepts'][change.concept], self.cram)
            self.assertEqual(warnings, [])
            result = subprocess.run(['git', '-C', str(self.root), 'apply', '--check', '-'],
                                    input=patch, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        washer = next(c for c in sync.compare(self.registry, self.cram, self.objects)
                      if c.concept == 'WashingMachine')
        patch, _ = sync.cram_patch(washer, self.registry['concepts']['WashingMachine'], self.cram)
        subprocess.run(['git', '-C', str(self.root), 'apply', '-'], input=patch, text=True, check=True)
        names = [n.name for n in ast.parse((self.root / sync.MODULE_FILE).read_text()).body
                 if isinstance(n, ast.ClassDef)]
        self.assertEqual(names.index('WashingMachine'), names.index('Dishwasher') + 1)
        self.assertTrue((self.root / sync.test_path('WashingMachine')).is_file())

    def test_registry_pull_request_changes_only_its_concept(self):
        adopt = next(c for c in sync.compare(self.registry, self.cram, self.objects) if c.kind == 'adopt')
        original = sync.REGISTRY
        sync.REGISTRY = self.root / 'semantic_concepts.json'
        self.addCleanup(setattr, sync, 'REGISTRY', original)
        sync.REGISTRY.write_text(json.dumps(self.registry, indent=1) + '\n')
        sync.ROOT, root = self.root, sync.ROOT
        self.addCleanup(setattr, sync, 'ROOT', root)
        patch = sync.registry_patch(adopt, self.registry, self.cram)
        changed = [l for l in patch.splitlines() if l[:1] in '+-' and not l.startswith(('+++', '---'))]
        self.assertEqual(changed, ['-   "cram": "missing"', '+   "cram": "available"'])


class RegistryTests(unittest.TestCase):
    def test_registry_is_consistent(self):
        registry = json.loads(sync.REGISTRY.read_text(encoding='utf-8'))
        statuses = {sync.AVAILABLE, sync.MISSING, sync.UNUSABLE}
        for name, entry in registry['concepts'].items():
            self.assertIn(entry['cram'], statuses, name)
            proposal = entry.get('proposal', {})
            if 'bases' in proposal:
                self.assertTrue(proposal['doc'], name)
        for object_type, concept in registry['object_types'].items():
            self.assertIn(concept, registry['concepts'], object_type)
        types = {o['fingerprint']['type'] for o in json.loads(sync.COLLECTION.read_text())['objects']}
        self.assertLessEqual(set(registry['object_types']), types, 'object type no object has')


if __name__ == '__main__':
    unittest.main()
