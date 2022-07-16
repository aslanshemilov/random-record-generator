import datetime
import unittest
from uuid import UUID

from faker import Faker

from generator.services.impl.faker_sales_record_generator import (
    FakerSalesRecordGenerator,
)


class TestFakerSalesRecordGenerator(unittest.TestCase):
    _under_test: FakerSalesRecordGenerator

    def setUp(self) -> None:
        self._under_test = FakerSalesRecordGenerator(Faker())
        return super().setUp()

    def test_generate_generates_id(self):
        result = self._under_test.generate()
        self.assertIsInstance(result.id, UUID)

    def test_generate_generates_widget_id(self):
        result = self._under_test.generate()
        self.assertIsInstance(result.widget_id, UUID)

    def test_generate_generates_customer_name(self):
        result = self._under_test.generate()
        self.assertIsInstance(result.customer_name, str)
        self.assertTrue(" " in result.customer_name)

    def test_generate_generates_category(self):
        result = self._under_test.generate()
        self.assertIsInstance(result.category, str)

    def test_generate_generates_price(self):
        result = self._under_test.generate()
        self.assertIsInstance(result.price, float)

    def test_generate_generates_created(self):
        result = self._under_test.generate()
        self.assertIsInstance(result.created, datetime.datetime)
