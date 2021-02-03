from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        try:
            ordered_list = []
            with open(filepath) as file:
                reader = csv.DictReader(file, delimiter=",", quotechar='"')
                for product in reader:
                    ordered_list.append(product)
            return ordered_list

        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")
