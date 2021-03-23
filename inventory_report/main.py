from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def main():
    try:
        zero, path, report_type = sys.argv

    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
        return

    if path.endswith('csv'):
        importer = CsvImporter

    elif path.endswith('json'):
        importer = JsonImporter

    else:
        importer = XmlImporter

    obj_instance = InventoryRefactor(importer)
    response = obj_instance.import_data(path, report_type)

    print(response, end="")
