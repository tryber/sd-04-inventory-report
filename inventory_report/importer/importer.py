from abc import abstractmethod


class Importer:
    @abstractmethod
    def import_data(file_path):
        raise NotImplementedError
