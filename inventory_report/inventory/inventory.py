import os

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.csv_importer import CsvImporter


class Inventory:

    @classmethod
    def import_data(cls, source_path, report_type):
        data = cls.import_datasource(source_path)

        if report_type == "completo":
            return CompleteReport.generate(data)
        else:
            return SimpleReport.generate(data)

    @classmethod
    def import_datasource(cls, source_path):
        file_extension = os.path.splitext(source_path)[1]

        if file_extension == '.csv':
            return CsvImporter.import_data(source_path)
        elif file_extension == '.json':
            return JsonImporter.import_data(source_path)
        else:
            return XmlImporter.import_data(source_path)
