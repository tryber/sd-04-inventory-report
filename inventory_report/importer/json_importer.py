import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('.json'):
            with open(path_file) as path_json:
                # reader_json = path_extension.read()
                data_file = json.load(path_json)
                return data_file
        else:
            return ValueError('Arquivo inválido')
