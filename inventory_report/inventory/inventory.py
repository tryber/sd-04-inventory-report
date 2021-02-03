import csv
import json
import xml
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if path.endswith(".csv"):
            with open(path) as file:
                data = list(csv.DictReader(file))
        if path.endswith(".json"):
            with open(path) as file:
                data = json.load(file)
        if path.endswith(".xml"):
            with open(path) as file:
                data = cls.import_xml(file)

        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @classmethod
    def import_xml(cls, file):
        tree = xml.etree.ElementTree.parse(file)
        root = tree.getroot()
        data = [] 
        for elemento in root:
            dicionario = {}
            for item in elemento:
                dicionario[item.tag] = item.text
            data.append(dicionario)
        return data
