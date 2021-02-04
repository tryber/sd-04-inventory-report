from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, pathname):
        if not pathname.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(pathname) as file:
            report = json.load(file)
        return report


# JsonImporter.import_data('inventory_report/data/inventory.json')
