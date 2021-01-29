import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory(CompleteReport, SimpleReport):
    def import_data(filepath, report_type):
        if filepath.endswith(".csv"):
            with open(filepath) as csv_file:
                reader = csv.DictReader(csv_file)
                data = list(reader)
                csv_file.close()

        if filepath.endswith(".json"):
            with open(filepath) as json_file:
                data = json.load(json_file)
                json_file.close()

        return (
            SimpleReport.generate(data)
            if report_type == "simples"
            else CompleteReport.generate(data)
        )
