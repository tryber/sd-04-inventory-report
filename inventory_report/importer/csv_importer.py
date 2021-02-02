import csv
from inventory_report.importer.importer import Importer


class CSVimporter(Importer):
    @classmethod
    def import_data(self, filepath):
        with open(filepath, encoding="utf-8") as file:
            data = []
            root = csv.DictReader(file, delimiter=",")
            for product in root:
                data.append(product)
            return data
