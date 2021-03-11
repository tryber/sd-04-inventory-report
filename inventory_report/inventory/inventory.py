import csv
import json
from reports import simple_report, complete_report


class Inventory:
    def simple_complete(self, data, tipe):
        if tipe == 'simples':
            return simple_report.generate(data)
        else:
            return complete_report.generate(data)

    def import_data(self, filepath, tipe):

        if filepath.endswith('.csv'):
            with open(filepath) as file:
                data = [csv.DictReader(file, delimiter=",")]
                self.simple_complete(data, tipe)

        elif filepath.endswith('.json'):
            with open(filepath) as file:
                data = file.read()
                data_json = json.loads(data)
                self.simple_complete(data_json, tipe)

        elif filepath.endswith('.xml'):
            with open(filepath) as file:
                data = file.read()
                simple_report(data, tipe)

        else:
            raise ValueError("Formato invalido")
