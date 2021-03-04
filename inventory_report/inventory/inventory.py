from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, path, tipo):
        report = []
        if path.endswith(".csv"):
            report = CsvImporter.import_data(path)
        if path.endswith(".json"):
            report = JsonImporter.import_data(path)
        if path.endswith(".xml"):
            report = XmlImporter.import_data(path)

        if tipo == "simples":
            return SimpleReport.generate(report)
        else:
            return CompleteReport.generate(report)
