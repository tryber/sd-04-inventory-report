from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_files(cls, file_path):
        if file_path.endswith(".csv"):
            return CsvImporter.import_data(file_path)
        elif file_path.endswith(".json"):
            return JsonImporter.import_data(file_path)
        elif file_path.endswith(".xml"):
            return XmlImporter.import_data(file_path)

    @classmethod
    def import_data(cls, path, report_type):
        data = cls.import_files(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
