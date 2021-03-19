from inventory_report.importer.importer import Importer
import csv


''' importer CSV simples ou completo'''


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(filepath) as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            info = [info for info in csv_reader]
        return info
