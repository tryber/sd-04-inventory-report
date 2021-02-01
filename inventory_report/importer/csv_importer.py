from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import CSVImporter


class CsvImporter(Importer):
    def import_data(filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        return CSVImporter.import_csv(filepath)
