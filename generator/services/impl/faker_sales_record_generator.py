from random import choice
from typing import List
from uuid import UUID
import uuid
from faker import Faker
from generator.domain.sales_record import SalesRecord
from generator.services.sales_record_generator import SalesRecordGenerator


class FakerSalesRecordGenerator(SalesRecordGenerator):
    """Generated ranom sales records using Faker.

    Attributes:
    _faker:       The Faker instance.
    _categories:  The list of categories in which to generate records.
    """

    _faker: Faker
    _categories: List[str]

    def __init__(self, faker: Faker, num_category: int = 5) -> None:
        self._faker = faker
        self._categories = self._populate_categories(num_category)
        super().__init__()

    def _populate_categories(self, num_category: int = 5) -> List[str]:
        return [self._faker.word() for _ in range(num_category)]

    def generate(self) -> SalesRecord:
        return SalesRecord(
            id=self._generate_uuid(),
            category=choice(self._categories),  # nosec
            widget_id=self._generate_uuid(),
            customer_name=self._faker.name(),
            price=self._generate_random_float(),
            created=self._faker.date_time(),
        )

    def _generate_random_float(self) -> float:
        return round(self._faker.pyfloat(positive=True), 2)


    def _generate_uuid(self) -> UUID:
        return uuid.uuid4()
