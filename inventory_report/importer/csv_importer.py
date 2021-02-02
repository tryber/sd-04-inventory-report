from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        products_list = []
        with open(filepath) as file:
            csv_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for product in csv_reader:
                products_list.append(product)
        return products_list
