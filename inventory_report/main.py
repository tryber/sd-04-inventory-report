import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    if sys.argv[1].endswith(".csv"):
        result = InventoryRefactor(CsvImporter).import_data(
            sys.argv[1], sys.argv[2]
        )
        print(result)
        return result

    elif sys.argv[1].endswith(".json"):
        result = InventoryRefactor(JsonImporter).import_data(
            sys.argv[1], sys.argv[2]
        )
        print(result)
        return result

    else:
        result = InventoryRefactor(XmlImporter).import_data(
            sys.argv[1], sys.argv[2]
        )
        print(result)
        return result


if __name__ == "__main__":
    main()
