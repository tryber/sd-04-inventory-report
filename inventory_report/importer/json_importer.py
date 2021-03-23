import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if not path_file.endswith(".json"):
            raise ValueError("Arquivo inválido")
        else:
            with open(path_file) as file:
                data = json.load(file)
                return data
