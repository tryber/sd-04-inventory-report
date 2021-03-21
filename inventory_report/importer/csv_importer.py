from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, source_path):
        if not source_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(source_path) as datasource:
            data = []
            root = csv.DictReader(datasource, delimiter=",")

            for product in root:
                data.append(product)

            return data
