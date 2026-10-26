import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from annotate_semantics import (CONCEPTS, SEMANTICS_FILE, SOURCE, moving_part_class, plan_object,
                                read_categories, read_objects, root_class, write_html)


class MovingPartTests(unittest.TestCase):
    def test_last_recognised_word_decides(self):
        self.assertEqual(moving_part_class(['b1', 'left', 'door'], 'revolute'), 'Door')
        self.assertEqual(moving_part_class(['right', 'door', 'handle'], 'revolute'), 'NaturalLanguageDescription')
        self.assertEqual(moving_part_class(['left', 'door', 'lever'], 'revolute'), 'NaturalLanguageDescription')

    def test_joint_type_must_fit(self):
        self.assertEqual(moving_part_class(['front', 'door'], 'prismatic'), 'Door')
        self.assertEqual(moving_part_class(['lower', 'rack'], 'prismatic'), 'Drawer')
        self.assertEqual(moving_part_class(['bin', 'r1c1'], 'revolute'), 'Drawer')
        self.assertEqual(moving_part_class(['lower', 'rack'], 'revolute'), 'NaturalLanguageDescription')
        self.assertEqual(moving_part_class(['lid'], 'continuous'), 'NaturalLanguageDescription')


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name)
        folder = self.source / 'kitchen/001-test'
        folder.mkdir(parents=True)
        (folder / 'model.urdf').write_text(
            '<robot name="t"><link name="t_body"/><link name="t_door"/><link name="t_door_grip"/>'
            '<link name="t_top_surface"/><link name="t_knob"/>'
            '<joint name="a" type="revolute"><parent link="t_body"/><child link="t_door"/></joint>'
            '<joint name="b" type="fixed"><parent link="t_door"/><child link="t_door_grip"/></joint>'
            '<joint name="c" type="fixed"><parent link="t_body"/><child link="t_top_surface"/></joint>'
            '<joint name="d" type="revolute"><parent link="t_door"/><child link="t_knob"/></joint></robot>')
        self.obj = {'folder': 'kitchen/001-test', 'slug': 't', 'name': 'Test',
                    'fingerprint': {'type': 'dishwasher'},
                    'frames': [{'name': 't_door_grip', 'purpose': 'grasp'},
                               {'name': 't_top_surface', 'purpose': 'place_surface'}]}

    def test_plan(self):
        plan = [(p.link, p.annotation, p.description) for p in plan_object(self.obj, self.source)]
        self.assertEqual(plan, [('t_body', 'Dishwasher', None), ('t_door', 'Door', None),
                                ('t_door_grip', 'Handle', None),
                                ('t_knob', 'NaturalLanguageDescription', 'knob')])

    def test_unknown_type_falls_back_to_a_description(self):
        self.obj['fingerprint']['type'] = 'angle grinder'
        root = plan_object(self.obj, self.source)[0]
        self.assertEqual((root.annotation, root.description, root.type_description),
                         ('NaturalLanguageWithTypeDescription', 'Test', 'angle grinder'))

    def test_html_page_embeds_the_graphs(self):
        obj = {**self.obj, 'id': '001', 'category': 'kitchen',
               'graph': {'nodes': [{'id': 't_body', 'annotation': 'Dishwasher', 'description': '</script>'}],
                         'edges': []}}
        page = write_html([obj], self.source / 'graph.html').read_text()
        self.assertNotIn('/*DATA*/[]', page)
        self.assertIn('"t_body"', page)
        self.assertEqual(page.count('</script>'), 2)

    def test_every_collection_object_can_be_planned(self):
        for obj in read_objects():
            self.assertTrue(plan_object(obj), obj['folder'])


class SemanticsFileTests(unittest.TestCase):
    """Every object's semantics.json still matches its model, the rules and its category."""

    def test_semantics_files_are_current(self):
        categories = read_categories()
        regenerate = 'regenerate with: annotate_semantics.py --write-semantics'
        for obj in read_objects():
            folder = SOURCE / obj['folder']
            with self.subTest(obj['folder']):
                path = folder / SEMANTICS_FILE
                self.assertTrue(path.is_file(), f'missing {path.name}; {regenerate}')
                document = json.loads(path.read_text(encoding='utf-8'))
                self.assertEqual(document['urdf'], 'model.urdf')
                self.assertEqual(document['object']['category'], obj['category'])
                self.assertEqual(document['object']['group'], categories[obj['category']]['group'], regenerate)
                planned = [{k: v for k, v in asdict(p).items() if v is not None} for p in plan_object(obj)]
                stored = [{k: v for k, v in a.items() if k not in ('attached_to', 'part_of', 'concept_status')}
                          for a in document['annotations']]
                self.assertEqual(stored, planned, regenerate)
                for annotation in document['annotations']:
                    if 'concept' in annotation:
                        self.assertEqual(annotation['concept_status'],
                                         CONCEPTS['concepts'][annotation['concept']]['cram'], regenerate)
                self.assertEqual(set(document['annotation_classes']), {a['annotation'] for a in stored})

                robot = ET.parse(folder / 'model.urdf').getroot()
                parents = {j.find('child').get('link'): j.find('parent').get('link') for j in robot.findall('joint')}
                for annotation in document['annotations']:
                    self.assertEqual(annotation['attached_to'], parents.get(annotation['link']))
                    ancestors, link = [], annotation['link']
                    while link in parents:
                        link = parents[link]
                        ancestors.append(link)
                    if annotation['part_of'] is not None:
                        self.assertIn(annotation['part_of'], ancestors, annotation['link'])


if __name__ == '__main__':
    unittest.main()
