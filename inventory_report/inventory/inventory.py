from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.complete_report import SimpleReport
import csv
import json
import xml


class Inventory(CompleteReport):
    @classmethod
    def csv_importer(self, filepath):
        try:
            ordered_list = []
            with open(filepath) as file:
                reader = csv.DictReader(file, delimiter=",", quotechar='"')
                for product in reader:
                    ordered_list.append(product)
            return ordered_list

        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")

    @classmethod
    def json_importer(self, filepath):
        try:
            with open(filepath) as file:
                return json.load(file)

        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")

    @classmethod
    def xml_importer(self, filepath):
        try:
            ordered_list = []
            for item in xml.etree.ElementTree.parse(filepath).getroot():
                product = {}
                for att in item:
                    product[att.tag] = att.text
                ordered_list.append(product)
            return ordered_list

        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")

    @classmethod
    def import_data(self, filepath, _type):

        if filepath.endswith(".csv"):
            should_call = self.csv_importer(filepath)

        elif filepath.endswith(".json"):
            should_call = self.json_importer(filepath)

        elif filepath.endswith(".xml"):
            should_call = self.xml_importer(filepath)

        if _type == "simples":
            return SimpleReport.generate(should_call)
        else:
            return CompleteReport.generate(should_call)
