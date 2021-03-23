from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, file_path):
        try:
            if not file_path.endswith('.json'):
                raise ValueError('Arquivo inválido')
            with open(file_path) as file:
                data_read = file.read()
                json_data = json.loads(data_read)
                return json_data
        except FileNotFoundError:
            raise ValueError('Arquivo não encontrado')
