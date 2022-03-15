from unittest import TestCase
from datetime import datetime

from settings import schemas
from tests.test_objects.add_months_datetimes import dates_one_month
from tests.test_objects.add_months_datetimes import dates_three_months
from tests.test_objects.amounts import input_data, output_data

import features


class TestFeatures(TestCase):

    def test_load_json(self):
        self.assertIsInstance(schemas.deposit_calc, dict)


    def test_validate_date(self):

        with self.assertRaises(ValueError):
            for date_str in ('31.02.2021', '31-02-2021', '31 Jan 2021'):
                features.validate_date(date_str)

        date_ = features.validate_date('01.01.2022')
        self.assertIsInstance(date_, datetime)


    def test_add_months(self):

        for key, value in dates_one_month.items():
            self.assertEqual(features.add_months(key), value)

        for key, value in dates_three_months.items():
            self.assertEqual(features.add_months(key,3), value)


    def test_calc_amount(self):
        self.assertEqual(features.calc_amount(input_data), output_data)
