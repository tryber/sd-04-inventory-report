import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory(CompleteReport, SimpleReport):
    def import_data(filepath, report_type):
        with open(filepath) as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
            csv_file.close()

        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
