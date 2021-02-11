from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def main():
    try:
        _arg1, pathfile, mode_report = sys.argv
    except ValueError:
        sys.stderr.write('Verifique os argumentos\n')
        return

    if pathfile.endswith('.csv'):
        reports = CsvImporter
    elif pathfile.endswith('.json'):
        reports = JsonImporter
    else:
        reports = XmlImporter

    refactor = InventoryRefactor(reports)
    result = refactor.import_data(pathfile, mode_report)
    print(result, end="")
