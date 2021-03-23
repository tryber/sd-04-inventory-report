import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

# https://www.guru99.com/manipulating-xml-with-python.html


class Inventory(SimpleReport, CompleteReport):
    @classmethod
    def read_csv(cls, file_csv):
        with open(file_csv, "r") as file:
            array_data = []
            reader = csv.DictReader(file, delimiter=',')
            for item in reader:
                array_data.append(item)
            return array_data

    @classmethod
    def read_json(cls, file_json):
        with open(file_json) as file:
            data = json.load(file)
            return data

    @classmethod
    def read_xml(cls, file_xml):
        tree = ET.parse(file_xml)
        root = tree.getroot()
        info = []
        for elem in root:
            elem_dict = {}
            for subelem in elem:
                elem_dict[subelem.tag] = subelem.text
            info.append(elem_dict)
        return info

    @classmethod
    def show_inventory(cls, file, tipo):
        if tipo == "simples":
            simple = SimpleReport.generate(file)
            print("simples")
            return simple
        else:
            complete = CompleteReport.generate(file)
            print("complete")
            return complete

    @classmethod
    def import_data(cls, file, tipo):
        if file.endswith(".csv"):
            new_csv = cls.read_csv(file)
            report = cls.show_inventory(new_csv, tipo)
            return report
        elif file.endswith(".json"):
            new_json = cls.read_json(file)
            report = cls.show_inventory(new_json, tipo)
            return report
        else:
            new_xml = cls.read_xml(file)
            report = cls.show_inventory(new_xml, tipo)
            return report
