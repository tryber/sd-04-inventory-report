from abc import ABC


class Importer(ABC):
    def import_data(self, pathname):
        raise NotImplementedError
