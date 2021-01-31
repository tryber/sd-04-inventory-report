from inventory_report.importer.importer import Importer
import xml


class XmlImporter(Importer):
    def import_data(self, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        ordered_list = []
        for item in xml.etree.ElementTree.parse(filepath).getroot():
            product = {}
            for att in item:
                product[att.tag] = att.text
            ordered_list.append(product)
        return ordered_list
