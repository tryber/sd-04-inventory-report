from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return
    main_path, file_path, file_type = sys.argv
    if file_path.endswith(".json"):
        importer = JsonImporter
    elif file_path.endswith(".xml"):
        importer = XmlImporter
    else:
        importer = CsvImporter

    inventory = InventoryRefactor(importer)
    print(inventory.import_data(file_path, file_type), end='')
