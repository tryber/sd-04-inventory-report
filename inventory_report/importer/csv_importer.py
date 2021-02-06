from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import CSVimporter


class CsvImporter(Importer):
    def import_data(file):
        if not file.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        return CSVimporter.import_csv(file)
