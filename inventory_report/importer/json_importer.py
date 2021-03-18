from .importer import Importer
from ..inventory.inventory import Inventory


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith("json"):
            raise ValueError("Arquivo inválido")
        return Inventory.import_data(path)
