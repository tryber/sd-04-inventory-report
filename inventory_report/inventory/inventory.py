from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(self, pathname, type):

        if pathname.endswith(".csv"):
            should_call = CsvImporter.import_data(pathname)

        elif pathname.endswith(".json"):
            should_call = JsonImporter.import_data(pathname)

        elif pathname.endswith(".xml"):
            should_call = XmlImporter.import_data(pathname)

        if type == "simples":
            return SimpleReport.generate(should_call)
        else:
            return CompleteReport.generate(should_call)
