from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def csv_reader(cls, pathname):
        with open(pathname) as file:
            csv_values = csv.DictReader(file, delimiter=",")
            values = [value for value in csv_values]

        return values

    @classmethod
    def json_reader(cls, pathname):
        with open(pathname) as file:
            json_values = json.load(file)

        return json_values

    @classmethod
    def xml_reader(cls, pathname):


    @classmethod
    def import_data(cls, pathname, type):
        final_report = []
        if pathname.endswith(".csv"):
            final_report = cls.csv_reader(pathname)
        elif pathname.endswith(".json"):
            final_report = cls.json_reader(pathname)
        elif pathname.endwith(".xml"):
            final_report = cls.xml_reader(pathname)

        if type == "simples":
            return SimpleReport.generate(final_report)
        elif type == "completo":
            return CompleteReport.generate(final_report)