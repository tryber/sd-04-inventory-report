from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter


class Inventory:
    def import_data(path, type):
        report = []
        if path.endswith(".csv"):
            report = CsvImporter.import_data(path)
        if path.endswith(".json"):
            report = JsonImporter.import_data(path)

        if type == "simples":
            return SimpleReport.generate(report)
        else:
            return CompleteReport.generate(report)
