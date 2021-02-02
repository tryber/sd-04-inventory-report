from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xml

classes = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    @classmethod
    def import_files(self, filepath):
        with open(filepath, encoding="utf-8") as file:
            if filepath.endswith(".csv"):
                data = []
                root = csv.DictReader(file, delimiter=",")
                for product in root:
                    data.append(product)
                return data

            elif filepath.endswith(".json"):
                data = json.load(file)

            else:
                data = []
                root = xml.etree.ElementTree.parse(file).getroot()
                for item in root:
                    product = {}
                    for parc in item:
                        product[parc.tag] = parc.text
                    data.append(product)
                return data

            return data

    @classmethod
    def import_data(self, path, report_type):
        data = Inventory.import_files(path)
        return classes[report_type].generate(data)
