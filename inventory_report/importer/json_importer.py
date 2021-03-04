from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            return data
