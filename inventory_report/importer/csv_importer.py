import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if not path_file.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        else:
            with open(path_file, "r") as file:
                array_data = []
                reader = csv.DictReader(file, delimiter=',')
                for item in reader:
                    array_data.append(item)
                return array_data
