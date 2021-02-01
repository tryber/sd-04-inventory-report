from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import XMLImporter


class XmlImporter(Importer):
    def import_data(filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        return XMLImporter.import_xml(filepath)
