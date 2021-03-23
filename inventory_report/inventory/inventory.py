from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def simp_or_comp(self, data, type):
        if type == 'simples':
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @classmethod
    def import_data(self, file_path, type):
        if file_path.endswith('.csv'):
            data_from_file = CsvImporter.import_data(file_path)
            return self.simp_or_comp(data_from_file, type)
