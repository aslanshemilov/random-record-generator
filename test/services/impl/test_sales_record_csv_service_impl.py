import os
import unittest

from faker import Faker
from generator.serializers.impl.sales_record_csv_serializer import (
    SalesRecordCsvSerializer,
)
from generator.services.impl.faker_sales_record_generator import (
    FakerSalesRecordGenerator,
)

from generator.services.impl.sales_record_csv_service_impl import (
    SalesRecordCsvServiceImpl,
)

dir_path = os.path.dirname(os.path.realpath(__file__))
tmp_dir = os.path.join(dir_path, "tmp")


class TestSalesRecordCsvServiceImpl(unittest.TestCase):
    _under_test: SalesRecordCsvServiceImpl

    def setUp(self) -> None:
        sales_record_generator = FakerSalesRecordGenerator(Faker(), 5)

        self._under_test = SalesRecordCsvServiceImpl(
            sales_record_generator, SalesRecordCsvSerializer()
        )
        if not os.path.exists(tmp_dir):
            os.mkdir(tmp_dir)

        return super().setUp()

    def test_write_writes_csv(self):
        out_path = os.path.join(tmp_dir, "test_write_writes_csv.csv")
        self._under_test.write(1, out_path)
        self.assertTrue(os.path.exists(out_path))

    def test_write_writes_csv_file_headers(self):
        out_path = os.path.join(tmp_dir, "test_write_writes_csv_file_headers.csv")
        self._under_test.write(1, out_path)
        with open(out_path) as result_file:
            result = result_file.readlines()
            self.assertTrue(len(result) > 0)

    def test_write_writes_csv_values(self):
        out_path = os.path.join(tmp_dir, "test_write_writes_csv_values.csv")
        self._under_test.write(1, out_path)
        with open(out_path) as result_file:
            result = result_file.readlines()
            self.assertTrue(len(result) == 2)

    def test_write_write_n_number_records(self):
        out_path = os.path.join(tmp_dir, "test_write_write_n_number_records.csv")
        self._under_test.write(50, out_path)
        with open(out_path) as result_file:
            result = result_file.readlines()
            self.assertTrue(len(result) == 51)
