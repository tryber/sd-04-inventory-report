from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import JSONImporter


class JsonImporter(Importer):
    def import_data(filepath):
        if not filepath.endswith(".json"):
            raise ValueError("Arquivo inválido")
        return JSONImporter.import_json(filepath)
