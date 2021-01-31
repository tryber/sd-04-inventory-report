from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, filepath, report_type):
        products = cls.import_products(filepath)
        return cls.generate_report(products, report_type)

    @classmethod
    def import_products(cls, filepath):
        if filepath.endswith(".csv"):
            return CsvImporter.import_data(filepath)
        elif filepath.endswith(".json"):
            return JsonImporter.import_data(filepath)
        elif filepath.endswith(".xml"):
            return XmlImporter.import_data(filepath)

    @classmethod
    def generate_report(cls, products_list, report_type):
        if report_type == "simples":
            return SimpleReport.generate(products_list)
        else:
            return CompleteReport.generate(products_list)
