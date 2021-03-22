import os
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        _, file_extension = os.path.splitext(path)

        if file_extension == ".csv":
            return cls.open_file(path, file_extension)
        else:
            raise ValueError("Arquivo inválido")
