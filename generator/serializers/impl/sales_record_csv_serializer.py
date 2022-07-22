from typing import List
from generator.serializers.csv_serializer import CsvSerializer


class SalesRecordCsvSerializer(CsvSerializer):
    """Serialized a sales record to a CSV-compatiable format."""

    def headers(self) -> List[str]:
        return ["id", "category", "widget_id", "customer_name", "price", "created"]

    def values(self, obj) -> List[str]:
        return [
            str(obj.id),
            obj.category,
            str(obj.widget_id),
            obj.customer_name,
            obj.price,
            obj.created.isoformat(),
        ]
