from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
import json
import csv
import os
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):

        _, file_extension = os.path.splitext(path)

        with open(path) as file:
            data = cls.load_file(cls, file_extension, file)

            if report_type == "simples":
                return SimpleReport.generate(data)

            if report_type == "completo":
                return CompleteReport.generate(data)

    def load_file(cls, file_extension, file):
        data = []
        if file_extension == ".csv":
            data = csv.DictReader(file)
            data = list(data)
            print(data)
        if file_extension == ".json":
            data = json.load(file)
        if file_extension == ".xml":
            data = cls.converter_xml(file)
        return data

    @classmethod
    def converter_xml(cls, file):

        tree = ET.parse(file)
        root = tree.getroot().findall("record")

        data = []

        for elem in root:
            dicionario = {}

            for item in elem:
                dicionario[item.tag] = item.text

            data.append(dicionario)

        return data
