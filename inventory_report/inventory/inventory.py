import csv
import json
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, report_type):
        if path.endswith(".csv"):
            with open(path) as file:
                data = list(csv.DictReader(file))
        if path.endswith(".json"):
            with open(path) as file:
                data = json.load(file)

        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
