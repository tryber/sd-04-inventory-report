from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(file_path) as file:
            return json.load(file)
