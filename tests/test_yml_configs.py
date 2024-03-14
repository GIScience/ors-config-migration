import unittest
from os.path import join, dirname

import yaml

from models.yml_config import OrsConfigYML


class YMLConfigTest(unittest.TestCase):
    def test_yml_config(self):
        in_file = '../config-files-yaml/application.yml'
        error_list = []
        with open(join(dirname(__file__), str(in_file)), 'r') as f:
            yaml_dict = yaml.load(f, Loader=yaml.FullLoader)

        OrsConfigYML.model_validate(yaml_dict)

    def test_test_yml_config(self):
        in_file = '../config-files-yaml/application-test.yml'
        error_list = []
        with open(join(dirname(__file__), str(in_file)), 'r') as f2:
            yaml_dict2 = yaml.load(f2, Loader=yaml.FullLoader)

        OrsConfigYML.model_validate(yaml_dict2)


    def test_unittest_yml_config(self):
        in_file = '../config-files-yaml/application-unittest.yml'
        error_list = []
        with open(join(dirname(__file__), str(in_file)), 'r') as f3:
            yaml_dict3 = yaml.load(f3, Loader=yaml.FullLoader)

        OrsConfigYML.model_validate(yaml_dict3)


if __name__ == '__main__':
    unittest.main()
