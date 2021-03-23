from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as path:
            root = ET.parse(path).getroot()
            data = []
            for child in root:
                obj = {}
                for neto in child:
                    obj[neto.tag] = neto.text
                data.append(obj)
            return data
