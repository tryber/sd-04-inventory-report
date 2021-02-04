from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def import_data(pathfile, mode_report):
        
        if pathfile.endswith('.csv'):
           reports = CsvImporter.import_data(pathfile)
        if pathfile.endswith('.json'):
            reports = JsonImporter.import_data(pathfile)
        if pathfile.endswith('.xml'):
            reports = XmlImporter.import_data(pathfile)
            
        if mode_report == 'simples':
            return SimpleReport.generate(reports)
        else:
            return CompleteReport.generate(reports)
