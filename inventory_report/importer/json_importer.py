from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        try:
            if not caminho.endswith(".json"):
                raise ValueError("Arquivo inválido")
            with open(caminho) as file:
                data = file.read()
                data_json = json.loads(data)
                return data_json
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")
