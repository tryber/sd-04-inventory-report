from inventory_report.importer.importer import Importer
import json


class JSONimporter(Importer):
    @classmethod
    def import_data(self, filepath):
        with open(filepath, encoding="utf-8") as file:
            data = json.load(file)
            return data
