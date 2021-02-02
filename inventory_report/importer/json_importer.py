from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if not filepath.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(filepath, encoding="utf-8") as file:
            data = json.load(file)
            return data
