from .importer import Importer
from ..inventory.inventory import Inventory


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith("xml"):
            raise ValueError("Arquivo inválido")
        return Inventory.import_data(path)
