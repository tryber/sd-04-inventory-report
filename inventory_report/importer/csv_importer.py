from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, pathname):
        # return super().import_data(pathname)
        if not pathname.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(pathname) as file:
            report_reader = csv.DictReader(file, delimiter=",")
            report = list(report_reader)
        return report


# CsvImporter.import_data('inventory_report/data/inventory.csv')
