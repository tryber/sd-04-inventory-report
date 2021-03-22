from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        if not caminho.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(caminho) as file:
            pai = ET.parse(file).getroot()
            data = []
            for filho in pai:
                obj = {}
                for neto in filho:
                    obj[neto.tag] = neto.text
                data.append(obj)
            return data
