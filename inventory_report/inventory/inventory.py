import csv
import json
import xml.etree.ElementTree as TREE
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

classes = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    def import_dict(path):
        with open(path, encoding="utf-8") as file:
            if path.endswith(".csv"):
                data = [data for data in csv.DictReader(file)]
            elif path.endswith(".json"):
                data = json.load(file)
            else:
                root = TREE.parse(file).getroot()
                data = [{el.tag: el.text for el in record} for record in root]

            return data

    def import_data(path, r_type):
        data = Inventory.import_dict(path)
        return classes[r_type].generate(data)


print(Inventory.import_data("inventory_report/data/inventory.xml", "simples"))
