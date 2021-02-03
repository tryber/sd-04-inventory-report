from ..importer.importer import Importer
import xml


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        tree = xml.etree.ElementTree.parse(path)
        root = tree.getroot()
        data = []
        for elemento in root:
            dicionario = {}
            for item in elemento:
                dicionario[item.tag] = item.text
            data.append(dicionario)
        return data
