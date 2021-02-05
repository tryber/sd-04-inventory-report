from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_files(cls, filepath):
        if filepath.endswith(".csv"):
            return CsvImporter.import_data(filepath)

        elif filepath.endswith(".json"):
            return JsonImporter.import_data(filepath)

        elif filepath.endswith(".xml"):
            return XmlImporter.import_data(filepath)

    @classmethod
    def import_data(cls, path, report_type):
        data = cls.import_files(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
