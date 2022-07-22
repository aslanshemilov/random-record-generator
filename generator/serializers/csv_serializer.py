from abc import ABC, abstractmethod
from typing import List


class CsvSerializer(ABC):
    """Serializes the provided object to CSV-compatiable format."""

    @abstractmethod
    def headers(self) -> List[str]:
        pass

    @abstractmethod
    def values(self, obj) -> List[str]:
        pass
