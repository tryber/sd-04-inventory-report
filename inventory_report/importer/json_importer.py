from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, source_path):
        if not source_path.endswith(".json"):
            raise ValueError("Invalid file format")

        # Opening JSON file
        with open(source_path) as datasource:
            return json.load(datasource)
