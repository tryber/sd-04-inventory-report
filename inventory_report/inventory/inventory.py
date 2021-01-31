from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, pathname, type):
        final_report = []
        if pathname.endswith(".csv"):
            final_report = CsvImporter.import_data(pathname)
        elif pathname.endswith(".json"):
            final_report = JsonImporter.import_data(pathname)
        elif pathname.endswith(".xml"):
            final_report = XmlImporter.import_data(pathname)

        if type == "simples":
            return SimpleReport.generate(final_report)
        else:
            return CompleteReport.generate(final_report)

# https://www.guru99.com/manipulating-xml-with-python.html
