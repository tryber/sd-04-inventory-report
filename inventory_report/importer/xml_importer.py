from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import XMLimporter


class XmlImporter(Importer):
    def import_data(file):
        if not file.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        return XMLimporter.import_xml(file)
