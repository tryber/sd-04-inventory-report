from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    try:
        _, path, report_type = sys.argv
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
        return
    if path.endswith(".json"):
        importer = JsonImporter
    elif path.endswith(".xml"):
        importer = XmlImporter
    else:
        importer = CsvImporter
    result = InventoryRefactor(importer).import_data(path, report_type)
    print(result, end="")
