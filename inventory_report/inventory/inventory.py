from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CSVImporter


class Inventory:
    def __init__(self):
        self = self

    @classmethod
    def import_data(cls, inventory_path, report_type):

        report = CSVImporter.import_data(inventory_path)

        simple_report = SimpleReport.generate(report)
        complete_report = CompleteReport.generate(report)

        if report_type == "simples":
            return simple_report
        else:
            return complete_report
