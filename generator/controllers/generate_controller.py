from generator.services.sales_record_csv_service import SalesRecordCsvService


class GenerateController:
    """CLI Controller for generating random sale records to CSV.

    Attributes:
        _csv_service: Service to write random sales records to CSV.
    """

    _csv_service: SalesRecordCsvService

    def __init__(self, csv_service: SalesRecordCsvService) -> None:
        self._csv_service = csv_service

    def generate(self, record_count: int, out_path: str) -> int:
        if record_count < 1:
            print("Record count must be greater than 0")
            return 1

        self._csv_service.write(record_count, out_path)
        return 0
