from abc import ABC, abstractmethod


class SalesRecordCsvService(ABC):
    @abstractmethod
    def write(self, record_count: int, out_path: str):
        pass
