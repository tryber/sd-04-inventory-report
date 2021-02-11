from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from xml.etree import ElementTree
import csv
import json


class Inventory:
    @classmethod
    def read_csv(cls, path):
        prod_list = []
        with open(path) as file:
            prod_csv = csv.DictReader(file, delimiter=",", quotechar='"')
            for elem in prod_csv:
                prod_list.append(elem)
        return prod_list

    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            prod_list = json.load(file)
            return prod_list

    @classmethod
    def read_xml(cls, path):
        root = ElementTree.parse(path).getroot()
        records = root.findall("record")
        records_list = []
        for elem in records:
            temp_dict = {}
            for e in elem:
                temp_dict[e.tag] = e.text
            records_list.append(temp_dict)
        return records_list

    @classmethod
    def import_data(cls, path, rel_type):
        prod_list = []
        if path.endswith(".csv"):
            prod_list = cls.read_csv(path)
        elif path.endswith(".json"):
            prod_list = cls.read_json(path)
        else:
            prod_list = cls.read_xml(path)
        if rel_type == "simples":
            return SimpleReport.generate(prod_list)
        else:
            return CompleteReport.generate(prod_list)
