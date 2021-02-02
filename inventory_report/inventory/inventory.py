from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

from inventory_report.importer.csv_importer import CSVimporter
from inventory_report.importer.json_importer import JSONimporter
from inventory_report.importer.xml_importer import XMLimporter


classes = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    @classmethod
    def import_files(self, filepath):
        if filepath.endswith(".csv"):
            return CSVimporter.import_data(filepath)

        elif filepath.endswith(".json"):
            return JSONimporter.import_data(filepath)

        elif filepath.endswith(".xml"):
            return XMLimporter.import_data(filepath)
        else:
            raise ValueError("Formato invalido")

    @classmethod
    def import_data(self, path, report_type):
        data = self.import_files(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
