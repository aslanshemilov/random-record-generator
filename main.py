
import argparse
import sys

from faker import Faker

from generator.controllers.generate_controller import GenerateController
from generator.serializers.impl.sales_record_csv_serializer import SalesRecordCsvSerializer
from generator.services.impl.faker_sales_record_generator import FakerSalesRecordGenerator
from generator.services.impl.sales_record_csv_service_impl import SalesRecordCsvServiceImpl

arg_count = 'count'
arg_out_path = 'out'

def main():
    parser = argparse.ArgumentParser(description='Generates random records')

    parser.add_argument(
        "--" + arg_count, type=int, help="The number of records to generate"
    )

    parser.add_argument(
        "--" + arg_out_path, type=str, help='File to write out to'
    )

    args = vars(parser.parse_args())

    sales_record_csv_serializer = SalesRecordCsvSerializer()

    sales_record_generator = FakerSalesRecordGenerator(
        Faker(), 5
    )

    sales_record_csv_service = SalesRecordCsvServiceImpl(
        sales_record_generator=sales_record_generator,
        sales_record_serializer=sales_record_csv_serializer,
    )

    generate_controller = GenerateController(
        csv_service=sales_record_csv_service,
    )

    record_count = args.get(arg_count)
    out_path = args.get(arg_out_path)

    print(f"Writing {record_count} records to path '{out_path}'")
    exit_code = generate_controller.generate(
        record_count=record_count,
        out_path=out_path,
    )
    sys.exit(exit_code)


if __name__ == '__main__':
    main()

