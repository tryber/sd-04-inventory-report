import csv
import json
import xml.etree.ElementTree as ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class JsonImporter:
    def import_json(path):
        with open(path) as json_file:
            return json.load(json_file)
            json_file.close()


class XmlImporter:
    def import_xml(path):
        element_tree = ElementTree.parse(path)
        root = element_tree.getroot()
        data = []

        for product in root:
            obj = {}
            for element in product:
                obj[element.tag] = element.text
                if obj not in data:
                    data.append(obj)
        return data


class CsvImporter:
    def import_csv(filepath):
        with open(filepath) as csv_file:
            file_reader = csv.DictReader(csv_file)
            return list(file_reader)
            csv_file.close()


"""
class Inventory:
    # def __init__(self, report_result)

    @classmethod
    def import_data(cls, imported_file, report_type):
        cls.report_result = ""
        with open(imported_file) as file:
            file_reader = csv.reader(file, delimiter=",")
            header, *data = file_reader
            file_result = [
                {header: data for header, data in zip(header, data)}
                for data in data
            ]
            if report_type == "simples":
                cls.report_result = SimpleReport.generate(file_result)
            elif report_type == "completo":
                cls.report_result = CompleteReport.generate(file_result)
            else:
                cls.report_result = "Tipo de relatório inválido"
            file.close()
        return cls.report_result """


# Inventory.import_data("inventory_report/data/inventory.csv", "completo")
class Inventory(CompleteReport, SimpleReport):

    @classmethod
    def import_data(cls, filepath, report_type):
        if filepath.endswith(".json"):
            data = JsonImporter.import_json(filepath)
        if filepath.endswith(".csv"):
            data = CsvImporter.import_csv(filepath)
        if filepath.endswith(".xml"):
            data = XmlImporter.import_xml(filepath)
        return (
            SimpleReport.generate(data)
            if report_type == "simples"
            else CompleteReport.generate(data)
            )


# filepath = "inventory_report/data/inventory.xml"
# reportType = "simples"
# didWork = Inventory.import_data(filepath, reportType)
# print(didWork)
