# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport
import csv
import json
from xml.dom import minidom

# classes = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    def import_data(path, report_type):
        with open(path, encoding="utf-8") as file:
            if path.endswith(".csv"):
                data = [data for data in csv.DictReader(file)]
            elif path.endswith(".json"):
                data = json.load(file)
            else:
                xml_records = minidom.parse(file).getElementsByTagName('record')
                # data = [{[element._get_tagName()]: element.value for element in record._get_childNodes()} for record in xml_records]
                print(xml_records[0].tagName)

            # return data
            # return classes[report_type].generate(data)


Inventory.import_data("inventory_report/data/inventory.xml", "simples")
