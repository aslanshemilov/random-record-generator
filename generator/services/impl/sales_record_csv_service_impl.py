import csv
from generator.serializers.impl.sales_record_csv_serializer import (
    SalesRecordCsvSerializer,
)
from generator.services.sales_record_csv_service import SalesRecordCsvService
from generator.services.sales_record_generator import SalesRecordGenerator


class SalesRecordCsvServiceImpl(SalesRecordCsvService):

    _sales_record_generator: SalesRecordGenerator
    _sales_record_serializer: SalesRecordCsvSerializer

    def __init__(
        self,
        sales_record_generator: SalesRecordGenerator,
        sales_record_serializer: SalesRecordCsvSerializer,
    ) -> None:
        self._sales_record_generator = sales_record_generator
        self._sales_record_serializer = sales_record_serializer
        super().__init__()

    def write(self, record_count: int, out_path: str):
        with open(out_path, "w+") as csv_file:
            csv_writer = csv.writer(csv_file)

            headers = self._sales_record_serializer.headers()
            csv_writer.writerow(headers)

            for _ in range(record_count):
                sales_record = self._sales_record_generator.generate()
                values = self._sales_record_serializer.values(sales_record)
                csv_writer.writerow(values)
