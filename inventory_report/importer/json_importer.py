from inventory_report.importer.importer import Importer
import json


''' importer JSON simples ou completo'''


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(filepath) as file:
            return(json.load(file))
