from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(filepath)
        root = tree.getroot()
        values = []

        for elem in root:
            obj = {}
            for subelem in elem:
                obj[subelem.tag] = subelem.text
            values.append(obj)
        return values
