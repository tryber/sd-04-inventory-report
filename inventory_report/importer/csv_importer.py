from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
