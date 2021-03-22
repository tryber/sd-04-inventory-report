from abc import abstractmethod
import csv
import json


class Importer:
    @abstractmethod
    def import_data(path):
        pass

    @classmethod
    def load_file(cls, file_extension, file):
        data = []
        if file_extension == ".csv":
            data = csv.DictReader(file)
            data = list(data)
        if file_extension == ".json":
            data = json.load(file)
        if file_extension == ".xml":
            data = cls.converter_xml(file)
        return data

    @classmethod
    def open_file(cls, path, file_extension):
        with open(path) as file:
            data = cls.load_file(file_extension, file)
            return data
