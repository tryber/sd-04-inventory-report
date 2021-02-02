from inventory_report.importer.importer import Importer
import xml


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        root = xml.etree.ElementTree.parse(filepath).getroot()
        products_list = []
        for elem in root:
            product = {}
            for sub_elem in elem:
                product[sub_elem.tag] = sub_elem.text
            products_list.append(product)
        return products_list
