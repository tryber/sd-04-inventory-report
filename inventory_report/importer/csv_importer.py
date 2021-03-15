from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path) as csv_file:
            data = []
            csv_reader = csv.DictReader(csv_file)
            for item in csv_reader:
                data.append(item)
            return data
