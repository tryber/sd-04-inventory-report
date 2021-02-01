import csv
import json
import xml.etree.ElementTree as ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class CSVImporter:
    def import_csv(filepath):
        with open(filepath) as csv_file:
            reader = csv.DictReader(csv_file)
            return list(reader)
            csv_file.close()


class JSONImporter:
    def import_json(filepath):
        with open(filepath) as json_file:
            return json.load(json_file)
            json_file.close()


class XMLImporter:
    def import_xml(filepath):
        tree = ElementTree.parse(filepath)
        root = tree.getroot()
        data = []

        for product in root:
            obj = {}
            for item in product:
                obj[item.tag] = item.text
                if obj not in data:
                    data.append(obj)

        return data


class Inventory(CompleteReport, SimpleReport):
    def import_data(filepath, report_type):
        if filepath.endswith(".csv"):
            data = CSVImporter.import_csv(filepath)

        if filepath.endswith(".json"):
            data = JSONImporter.import_json(filepath)

        if filepath.endswith(".xml"):
            data = XMLImporter.import_xml(filepath)

        return (
            SimpleReport.generate(data)
            if report_type == "simples"
            else CompleteReport.generate(data)
        )
