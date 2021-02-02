from inventory_report.importer.importer import Importer
import json


class JSONImporter(Importer):
    @classmethod
    def import_data(cls, pathname):
        if not pathname.endswith(".json"):
            raise ValueError("Formato invalido")
        with open(pathname) as file:
            report = json.load(file)
        return report


# JSONImporter.import_data('inventory_report/data/inventory.json')
