from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(self, filepath):
        if not filepath.endswith(".json"):
            raise ValueError("Arquivo inválido")
        try:
            with open(filepath) as file:
                return json.load(file)

        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")