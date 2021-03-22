from .importer import Importer
from ..inventory.inventory import Inventory


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith("csv"):
            raise ValueError("Arquivo inválido")
        return Inventory.import_file(path)
