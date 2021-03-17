from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as ET
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, file_path, type):
        report = []
        if file_path.endswith(".csv"):
            report = cls.reader_csv(file_path)
        elif file_path.endswith(".json"):
            report = cls.reader_json(file_path)
        else:
            report = cls.reader_xml(file_path)

        if type == "simples":
            return SimpleReport.generate(report)
        elif type == "completo":
            return CompleteReport.generate(report)

    @classmethod
    def reader_csv(cls, file_path):
        with open(file_path) as file:
            csv_file = csv.DictReader(file, delimiter=",")
            return [row for row in csv_file]

    @classmethod
    def reader_json(cls, file_path):
        with open(file_path) as file:
            return json.load(file)

    # https://docs.python.org/3/library/xml.etree.elementtree.html
    @classmethod
    def reader_xml(cls, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        xml_list = []

        # acessar elementos e subelementos do XML
        # x = <record>
        # y = <tag>text</tag>
        for x in root:
            inventory = {}
            for y in x:
                inventory[y.tag] = y.text
            xml_list.append(inventory)
        return xml_list
