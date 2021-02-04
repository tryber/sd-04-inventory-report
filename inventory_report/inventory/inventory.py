from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    # def __init__(self):
    #     self = self

    @classmethod
    def import_data(cls, inventory_path, report_type):

        if inventory_path.endswith(".csv"):
            report = CsvImporter.import_data(inventory_path)
        elif inventory_path.endswith(".json"):
            report = JsonImporter.import_data(inventory_path)
        elif inventory_path.endswith(".xml"):
            report = XmlImporter.import_data(inventory_path)

        simple_report = SimpleReport.generate(report)
        complete_report = CompleteReport.generate(report)

        if report_type == "simples":
            return simple_report
        else:
            return complete_report
