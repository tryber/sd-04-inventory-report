from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    try:
        _, filepath, report_type = sys.argv
    except ValueError:
        print(f"Verifique os argumentos {file=sys.stderr}")
        return
    importer = ""
    if filepath.endswith(".csv"):
        importer = CsvImporter
    elif filepath.endswith(".json"):
        importer = JsonImporter
    elif filepath.endswith(".xml"):
        importer = XmlImporter
    instance = InventoryRefactor(importer)
    report_result = instance.import_data(filepath, report_type)
    print(report_result, end="")
