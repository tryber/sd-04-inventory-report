from .importer import Importer
import os
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        _, file_extension = os.path.splitext(path)

        if file_extension == ".xml":
            return cls.open_file(path, file_extension)
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
