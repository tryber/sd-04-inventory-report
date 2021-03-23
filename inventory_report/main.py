from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    pass
    try:
        _, path, type_of_file = sys.argv
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
        return
    if path.endswith(".json"):
        importer = JsonImporter
    elif path.endswith(".xml"):
        importer = XmlImporter
    else:
        importer = CsvImporter
    result_import = InventoryRefactor(importer).import_data(path, type_of_file)
    print(result_import, end="")
