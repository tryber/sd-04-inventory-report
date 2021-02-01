from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xml


class Inventory:
    @classmethod
    def csv_reader(self, pathname):
        with open(pathname) as file:
            csv_values = csv.DictReader(file, delimiter=",")
            values = [value for value in csv_values]
        return values

    @classmethod
    def json_reader(self, pathname):
        with open(pathname) as file:
            json_values = json.load(file)

        return json_values

    @classmethod
    def xml_reader(self, pathname):
        values = []

        for elem in xml.etree.ElementTree.parse(pathname).getroot():
            obj = {}
            for subelem in elem:
                obj[subelem.tag] = subelem.txt
            values.append(obj)
        return values

    @classmethod
    def import_data(self, pathname, type):

        if pathname.endswith(".csv"):
            should_call = self.csv_reader(pathname)

        elif pathname.endswith(".json"):
            should_call = self.json_reader(pathname)

        elif pathname.endswith(".xml"):
            should_call = self.xml_reader(pathname)

        if type == "simples":
            return SimpleReport.generate(should_call)
        else:
            return CompleteReport.generate(should_call)
