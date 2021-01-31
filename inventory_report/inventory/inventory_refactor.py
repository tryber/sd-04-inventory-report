from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
import os
import xml.etree.ElementTree as ET
from ..importer.json_importer import JsonImporter
from ..importer.csv_importer import CsvImporter
from ..importer.xml_importer import XmlImporter
from collections.abc import Iterable
from .inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(cls):
        cls._inventory = []

    @classmethod
    def add_item(cls, lista):
        cls._inventory.extend(lista)

    def __iter__(cls):
        return InventoryIterator(cls.__inventory)

    @classmethod
    def import_data(cls, path, report_type):

        _, file_extension = os.path.splitext(path)

        with open(path) as file:
            data = cls.load_file(file_extension, file)

            cls.add_item(data)

            if report_type == "simples":
                return SimpleReport.generate(data)

            if report_type == "completo":
                return CompleteReport.generate(data)

    def load_file(file_extension, file):
        if file_extension == ".csv":
            return CsvImporter.import_data(file)
        if file_extension == ".json":
            return JsonImporter.import_data(file)
        if file_extension == ".xml":
            return XmlImporter.import_data(file)
        else:
            raise ValueError("Arquivo inválido")

    @classmethod
    def converter_xml(cls, file):

        tree = ET.parse(file)
        root = tree.getroot().findall("record")

        data = []

        for elem in root:
            dicionario = {}

            for item in elem:
                dicionario[item.tag] = item.text

            data.append(dicionario)

        return data
