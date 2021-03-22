import os
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        _, file_extension = os.path.splitext(path)

        if file_extension == ".json":
            return cls.open_file(path, file_extension)
        else:
            raise ValueError("Arquivo inválido")
