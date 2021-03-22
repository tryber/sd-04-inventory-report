from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import csv
import json
from xml.etree import ElementTree


class Inventory:
    @classmethod
    def import_file(cls, path):
        with open(path, encoding="utf-8") as opened_file:
            if path.endswith("json"):
                imported_file = json.load(opened_file)
            elif path.endswith("csv"):
                imported_file = [item for item in csv.DictReader(opened_file)]
            elif path.endswith("xml"):
                file_root = ElementTree.parse(opened_file).getroot()
                imported_file = [
                    {element.tag: element.text for element in record}
                    for record in file_root
                ]
            return imported_file

    def import_data(path, report_type):
        imported_data = Inventory.import_file(path)
        
        return (
            SimpleReport.generate(imported_data)
            if report_type == "simples"
            else CompleteReport.generate(imported_data)
        )
