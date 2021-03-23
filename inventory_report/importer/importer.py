from abc import abstractmethod
# https://docs.python.org/pt-br/3.7/library/abc.html
# nao consegui dar o push


class Importer:
    @abstractmethod
    def import_data(caminho):
        raise NotImplementedError
