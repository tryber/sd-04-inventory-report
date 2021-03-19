from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    try:
        _argm1, file_path, mode_report = sys.argv
    except ValueError:
        sys.stderr.write('Verifique os argumentos\n')
        return

    if file_path.endswith(".csv"):
        reports = CsvImporter
    elif file_path.endswith(".json"):
        reports = JsonImporter
    else:
        reports = XmlImporter

    refactor = InventoryRefactor(reports)
    result = refactor.import_data(file_path, mode_report)
    print(result, end="")
