from abc import ABC, abstractmethod


class SalesRecordCsvService(ABC):
    """Writes the defined number of random sales record to a CSV."""

    @abstractmethod
    def write(self, record_count: int, out_path: str):
        pass
