import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if not path_file.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        else:
            tree = ET.parse(path_file)
            root = tree.getroot()
            info = []
            for elem in root:
                elem_dict = {}
                for subelem in elem:
                    elem_dict[subelem.tag] = subelem.text
                info.append(elem_dict)
            return info
