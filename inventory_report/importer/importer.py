import os
from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(self, path_file):
        if not os.path.exists(path_file):
            raise NotImplementedError
