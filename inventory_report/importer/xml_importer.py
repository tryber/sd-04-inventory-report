from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        root = ET.parse(filepath).getroot()
        data = []
        for elem in root:
            prod = {}
            for e_elem in elem:
                prod[e_elem.tag] = e_elem.text
            data.append(prod)
        return data
