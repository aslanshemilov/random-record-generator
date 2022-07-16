import unittest
from unittest.mock import MagicMock

from generator.controllers.generate_controller import GenerateController


class TestGenerateController(unittest.TestCase):
    _mock_csv_service: MagicMock
    _under_test: GenerateController

    def setUp(self) -> None:
        self._mock_csv_service = MagicMock()
        self._under_test = GenerateController(self._mock_csv_service)
        return super().setUp()

    def test_generate_exits_with_error_record_count_less_than_one(self):
        result = self._under_test.generate(0, "/path/to/csv.csv")
        self.assertEqual(1, result)

    def test_generate_calls_csv_service(self):
        record_count = 100
        out_path = "/path/to/csv.csv"
        self._under_test.generate(record_count, out_path)
        self._mock_csv_service.write.assert_called_with(record_count, out_path)
