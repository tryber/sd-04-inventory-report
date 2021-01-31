from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(filepath) as file:
            csv_values = csv.DictReader(file, delimiter=",")
            values = [value for value in csv_values]
        return values
