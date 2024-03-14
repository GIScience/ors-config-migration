import unittest
from os.path import join, dirname

import json

from pydantic import ValidationError

from models.json_config import OrsConfigJSON, Parameters, ProfileEntry


class JSONConfigTest(unittest.TestCase):
    def test_test_config(self):
        in_file = '../config-files-json/test-config.json'
        error_list = []
        with open(join(dirname(__file__), str(in_file)), 'r') as f:
            json_dict = json.load(f)

        OrsConfigJSON.model_validate(json_dict)

        self.validate_profiles(json_dict, error_list)
        if error_list:
            raise ExceptionGroup(f"Additional Config Properties found:", error_list)

    def test_car_config(self):
        in_file = '../config-files-json/ors-config.driving-car.json'
        error_list = []
        with open(join(dirname(__file__), str(in_file)), 'r') as f2:
            json_dict2 = json.load(f2)

        OrsConfigJSON.model_validate(json_dict2)

        self.validate_profiles(json_dict2, error_list)
        if error_list:
            raise ExceptionGroup(f"Additional Config Properties found:", error_list)

    def test_sample_config(self):
        in_file = '../config-files-json/ors-config-sample.json'
        error_list = []
        with open(join(dirname(__file__), str(in_file)), 'r') as f3:
            json_dict3 = json.load(f3)

        OrsConfigJSON.model_validate(json_dict3)

        self.validate_profiles(json_dict3, error_list)

        if error_list:
            raise ExceptionGroup(f"Additional Config Properties found:", error_list)

    def validate_profiles(self, json_dict, error_list):
        profiles = json_dict['ors']['services']['routing']['profiles']
        for key, value in profiles.items():
            if key == "active":
                self.assertIsInstance(value, list)
                for entry in value:
                    self.assertIsInstance(entry, str)
            if key == "default_params":
                try:
                    Parameters.model_validate(value)
                except ValidationError as e:
                    format_e = '\n'.join(str(e).split('\n')[:2])
                    print(f"Unknown config property found in 'ors.services.routing.profiles.default_parameters': {format_e}")
                    error_list.append(e)
                    print()
            if key.startswith("profile-"):
                try:
                    ProfileEntry.model_validate(value)
                except ValidationError as e:
                    format_e = '\n'.join(str(e).split('\n')[:2])
                    print(f"Unknown config property found in 'ors.services.routing.profiles.{key}': {format_e}")
                    error_list.append(e)
                    print()


if __name__ == '__main__':
    unittest.main()
