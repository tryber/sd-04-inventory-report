import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if path_file.endswith('.json'):
            with open(path_file) as path_json:
                # reader_json = path_extension.read()
                data_file = json.load(path_json)
                return data_file
        else:
            raise ValueError('Arquivo inválido')
