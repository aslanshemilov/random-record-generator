import datetime
import unittest
import uuid
from generator.domain.sales_record import SalesRecord

from generator.serializers.impl.sales_record_csv_serializer import (
    SalesRecordCsvSerializer,
)


class TestSalesRecordCsvSerializer(unittest.TestCase):
    _sales_record: SalesRecord
    _under_test: SalesRecordCsvSerializer

    def setUp(self) -> None:
        self._under_test = SalesRecordCsvSerializer()
        return super().setUp()

    def test_headers_returns_headers(self):
        result = self._under_test.headers()
        expected = ["id", "category", "widget_id", "customer_name", "price", "created"]
        self.assertEqual(expected, result)

    def test_values_returns_correct_values(self):
        sales_record = SalesRecord(
            id=uuid.UUID("93cfd26c-c8e7-4a31-9565-3943ef1aae12"),
            category="blue",
            widget_id=uuid.UUID("3ab5a1f4-1de7-4ada-b01d-bbb2af52d35c"),
            customer_name="John Doe",
            price=123.45,
            created=datetime.datetime(2022, 7, 1, 13, 00, 00),
        )
        result = self._under_test.values(sales_record)
        expected = [
            "93cfd26c-c8e7-4a31-9565-3943ef1aae12",
            "blue",
            "3ab5a1f4-1de7-4ada-b01d-bbb2af52d35c",
            "John Doe",
            123.45,
            "2022-07-01T13:00:00",
        ]
        self.assertEqual(expected, result)
