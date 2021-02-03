import csv
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, report_type):
        with open(path) as file:
            data = list(csv.DictReader(file))

        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)