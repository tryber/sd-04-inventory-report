from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.complete_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:

    @classmethod
    def import_data(self, filepath, _type):

        if filepath.endswith(".csv"):
            should_call = CsvImporter.import_data(self, filepath)

        elif filepath.endswith(".json"):
            should_call = JsonImporter.import_data(self, filepath)

        elif filepath.endswith(".xml"):
            should_call = XmlImporter.import_data(self, filepath)

        if _type == "simples":
            return SimpleReport.generate(should_call)
        else:
            return CompleteReport.generate(should_call)
