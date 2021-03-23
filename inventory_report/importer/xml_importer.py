from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET
# https://docs.python.org/pt-br/3/library/xml.etree.elementtree.html
# ?highlight=elementtree#module-xml.etree.ElementTree


class XmlImporter(Importer):
    @classmethod
    def import_data(self, file_path):
        if not file_path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        with open(file_path) as file:
            tree = ET.parse(file)
            root = tree.getroot()
            data = []
            for x in root:
                dic = {}
                for y in x:
                    dic[y.tag] = y.text
                data.append(dic)
            return data
