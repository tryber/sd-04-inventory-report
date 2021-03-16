from abc import abstractmethod


class Importer:
    @abstractmethod
    def import_data(file):
        raise NotImplementedError
