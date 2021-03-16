from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(file_path)
        root = tree.getroot()
        xml_list = []

        for x in root:
            inventory = {}
            for y in x:
                inventory[y.tag] = y.text
            xml_list.append(inventory)
        return xml_list
