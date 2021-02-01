from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
