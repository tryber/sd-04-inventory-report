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
    if path.endswith(".csv"):
        importer = CsvImporter
    elif path.endswith(".json"):
        importer = JsonImporter
    else:
        importer = XmlImporter
    instance = InventoryRefactor(importer)
    result = instance.import_data(path, report_type)
    print(result, end="")
