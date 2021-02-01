import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(pathname):
        if pathname.endswith(".csv"):
            with open(pathname) as file:
                csv_values = csv.DictReader(file, delimiter=",")
                values = [value for value in csv_values]
            return values
        else:
            raise ValueError("Arquivo inválido")
