from abc import ABC, abstractmethod


''' req 6 '''


class Importer(ABC):
    ''' classe abstrata para implementação das herdeiras'''
    ''' classes herdeiras: CsvImporter, JsonImporter e XmlImporter'''
    @abstractmethod
    def import_data(path):
        raise NotImplementedError
