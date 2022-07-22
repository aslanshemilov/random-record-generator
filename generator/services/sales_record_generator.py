from abc import ABC, abstractmethod

from generator.domain.sales_record import SalesRecord


class SalesRecordGenerator(ABC):
    """Generates a random sales Record."""

    @abstractmethod
    def generate(self) -> SalesRecord:
        pass
