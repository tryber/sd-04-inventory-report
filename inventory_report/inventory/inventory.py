from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def simp_or_comp(self, data, tipo):
        if tipo == 'simples':
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @classmethod
    def import_data(self, file_path, tipo):
        if file_path.endswith('.csv'):
            data_from_file = CsvImporter.import_data(file_path)
            return self.simp_or_comp(data_from_file, tipo)
        elif file_path.endswith('.json'):
            data_from_file = JsonImporter.import_data(file_path)
            return self.simp_or_comp(data_from_file, tipo)
        elif file_path.endswith('.xml'):
            data_from_file = XmlImporter.import_data(file_path)
            return self.simp_or_comp(data_from_file, tipo)

