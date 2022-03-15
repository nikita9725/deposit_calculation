from unittest import TestCase
from jsonschema import validate, ValidationError

from app import app
from settings import config, schemas

from tests.test_objects.test_requests_data import wrong_input_data_list
from tests.test_objects.amounts import input_data ,output_data


class TestApp(TestCase):

    def test_config(self):
        self.assertIsInstance(config.log_path, str)
        self.assertIsInstance(config.flask_app_config, dict)


    def test_validation(self):

        with self.assertRaises(ValidationError):

            for wrong_data in wrong_input_data_list:
                validate(wrong_data, schemas.deposit_calc)


    def test_deposit_calc_endpoint(self):
        tester = app.test_client(self)
        resp = tester.post('/deposit_calc', json=input_data)
        self.assertEqual(resp.get_json(), dict(output_data))
