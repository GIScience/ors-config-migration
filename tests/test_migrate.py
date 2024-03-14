import os
import shutil
from os.path import join, dirname
from unittest import TestCase

from migrate import migrate, if_exists_move_to


class Test(TestCase):
    def setUp(self):
        if os.path.exists('./outputs'):
            shutil.rmtree('./outputs')
        os.mkdir('./outputs')

    def test_migrate(self):
        in_file = '../config-files-json/test-config.json'

        migrate(join(dirname(__file__), in_file), "./outputs/test-config-migrated.yml")
        self.fail()

    def test_if_exists_move_to(self):
        test_dict = {"info": {
            "base_url": "https://allyourbasearebelongtous.com",
            "swagger_documentation_url": "/swagger-ui",
            "nest": {
                "path": ["this", 15, False],
                "deeper": {
                    "thats": "it"
                },
                "someBool": False,
                "someInt": 2,
                "someStr": "hello world"
            },
            "1":{"2":{"3": "Move away"}}
        }}
        if_exists_move_to(test_dict, 'info.nest.deeper', 'new.deep2')

        self.assertDictEqual(test_dict.get('new').get('deep2'), {"thats": "it"}, "Move to not working")
        self.assertNotIn('deeper', test_dict.get('info').get('nest'), "Origin not removed")
        if_exists_move_to(test_dict, 'info.swagger_documentation_url', 'new.deep2')

        if_exists_move_to(test_dict, 'info.1.2.3', '4')
        self.assertNotIn('1', test_dict.get('info'), "Empty Origin kept.")
        self.assertIn('4', test_dict, "Not moved to location")
