from inventory_report.importer.importer import Importer
import csv


class CSVImporter(Importer):
    @classmethod
    def import_data(cls, pathname):
        # return super().import_data(pathname)
        try:
            if not pathname.endswith(".csv"):
                raise ValueError("Formato invalido")
            with open(pathname) as file:
                report_reader = csv.DictReader(file, delimiter=",")
                report = list(report_reader)
        except FileNotFoundError:
            raise ValueError(
                "Arquivo tests/file_not_exist.csv não encontrado"
            )
        else:
            return report


# CSVImporter.import_data('inventory_report/data/inventory.csv')
