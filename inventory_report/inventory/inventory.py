import csv

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, imported_file, report_type):
        with open(imported_file) as file:
            file_reader = csv.reader(file, delimiter=",")
            header, *data = file_reader
            file_result = [
                {header: data for header, data in zip(header, data)}
                for data in data
            ]
            simple_report_result = SimpleReport.generate(file_result)
            print(simple_report_result)


# Inventory.import_data("inventory_report/data/inventory.csv", "simples")
