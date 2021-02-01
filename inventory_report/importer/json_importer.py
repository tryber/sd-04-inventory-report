import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
  def import_data(pathname):
    if pathname.endswith(".json"):
      with open(pathname) as file:
        json_values = json.load(file)

        return json_values
    else:
      raise ValueError("Arquivo inválido")
