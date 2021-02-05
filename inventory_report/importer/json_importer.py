from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import JSONimporter


class JsonImporter(Importer):
    def import_data(file):
        if not file.endswith(".json"):
            raise ValueError("Arquivo inválido")
        return JSONimporter.import_json(file)
