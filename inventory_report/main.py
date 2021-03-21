import sys
import os

from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor

importers = {
    ".json": JsonImporter,
    ".csv": CsvImporter,
    ".xml": XmlImporter
}


def main():
    try:
        nothing, source_path, report_type = sys.argv
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
        return

    importer = importers[os.path.splitext(source_path)[1]]

    import_data_instance = InventoryRefactor(importer)
    result = import_data_instance.import_data(source_path, report_type)

    print(result, end="")
