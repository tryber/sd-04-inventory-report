from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(filepath) as file:
            data = []
            root = csv.DictReader(file, delimiter=",")
            for product in root:
                data.append(product)
            return data
