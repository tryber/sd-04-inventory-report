from abc import abstractmethod
# https://docs.python.org/pt-br/3.7/library/abc.html


class Importer:
    @abstractmethod
    def import_data(caminho):
        raise NotImplementedError
