from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    p1 = sys.argv[1]
    p2 = sys.argv[2]
    ftd = []
    if p1.endswith('.csv'):
        ftd = InventoryRefactor(CsvImporter).import_data(p1, p2)
    elif p1.endswith('.json'):
        ftd = InventoryRefactor(JsonImporter).import_data(p1, p2)
    elif p1.endswith('.xml'):
        ftd = InventoryRefactor(XmlImporter).import_data(p1, p2)

    print(ftd)
    return ftd


if __name__ == "__main__":
    main()
