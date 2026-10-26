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

    def test_pull_requests_are_found_on_github_by_their_branch(self):
        asked = []

        def find(repository, owner, branch):
            asked.append((repository, owner, branch))
            return {'semantics/add-class-washing-machine': sync.PullRequest('u1', sync.OPEN),
                    'semantics/add-bases-chair': sync.PullRequest('u2', sync.CLOSED)}.get(branch)

        changes = sync.compare(self.registry, self.cram, self.objects)
        problem = sync.look_up_pull_requests(changes, self.registry,
                                             {'cram2': 'me', 'private_meshes': 'me'}, find)
        self.assertIsNone(problem)
        states = {c.slug: c.pull_request and c.pull_request.state for c in changes}
        self.assertEqual(states, {'adopt-dishwasher': None, 'add-bases-chair': sync.CLOSED,
                                  'add-class-washing-machine': sync.OPEN, 'map-type-sofa': None})
        self.assertIn(('cram2/x', 'me', 'semantics/add-class-washing-machine'), asked)
        self.assertIn((sync.PRIVATE_MESHES_REPOSITORY, 'me', 'semantics/adopt-dishwasher'), asked)

    def test_unreachable_github_is_reported_not_fatal(self):
        def find(repository, owner, branch):
            raise sync.GitHubUnavailable('offline')
        changes = sync.compare(self.registry, self.cram, self.objects)
        self.assertEqual(sync.look_up_pull_requests(changes, self.registry, {'cram2': 'me', 'private_meshes': 'me'},
                                                    find), 'offline')
        self.assertTrue(all(c.pull_request is None for c in changes))

    def test_declined_by_hand_is_not_proposed_again_until_cram2_has_it(self):
        self.registry['concepts']['Chair']['cram'] = sync.DECLINED
        self.assertNotIn('add-bases-chair', {c.slug for c in sync.compare(self.registry, self.cram, self.objects)})
        (self.root / sync.MODULE_FILE).write_text(MODULE.replace('class Chair(Furniture)', 'class Chair(Furniture, HasRootBody)'))
        cram = sync.CramClasses.read(self.root)
        self.assertIn('adopt-chair', {c.slug for c in sync.compare(self.registry, cram, self.objects)})

    def test_unassigned_types_are_listed_with_similar_concepts(self):
        self.registry['object_types']['furniture'] = None  # decided: stays on the fallback
        self.objects.append(obj('007', 'swivel chair'))
        self.assertEqual(list(sync.unassigned_types(self.registry, self.objects)), ['sofa', 'swivel chair'])
        self.assertEqual(sync.similar_concepts('swivel chair', self.registry, self.cram), ['Chair', 'OfficeChair'])

    def test_prepare_replaces_its_earlier_folders_but_nothing_else(self):
        out = self.root / 'out'
        stale = out / '03-cram2-add-class-old-thing'
        stale.mkdir(parents=True)
        (stale / 'PR.md').write_text('old')
        sync.clear_output(out)
        self.assertEqual(list(out.iterdir()), [])
        (out / 'notes.txt').write_text('mine')
        with self.assertRaises(SystemExit):
            sync.clear_output(out)
        self.assertTrue((out / 'notes.txt').is_file())

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
        statuses = {sync.AVAILABLE, sync.MISSING, sync.UNUSABLE, sync.DECLINED}
        for name, entry in registry['concepts'].items():
            self.assertIn(entry['cram'], statuses, name)
            proposal = entry.get('proposal', {})
            if 'bases' in proposal:
                self.assertTrue(proposal['doc'], name)
        for object_type, concept in registry['object_types'].items():
            if concept is not None:  # null: kept on the fallback on purpose
                self.assertIn(concept, registry['concepts'], object_type)
        types = {o['fingerprint']['type'] for o in json.loads(sync.COLLECTION.read_text())['objects']}
        self.assertLessEqual(set(registry['object_types']), types, 'object type no object has')


if __name__ == '__main__':
    unittest.main()
