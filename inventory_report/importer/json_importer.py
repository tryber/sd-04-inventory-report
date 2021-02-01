from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(filepath):
        if not filepath.endswith(".json"):
            raise ValueError("Arquivo inválido")
