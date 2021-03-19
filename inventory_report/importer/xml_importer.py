from inventory_report.importer.importer import Importer
import xml


''' importer XML simples ou completo'''


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        root = xml.etree.ElementTree.parse(filepath).getroot()
        lista_produtos = []
        for elem in root:
            obj = {}
            for sub_elem in elem:
                obj[sub_elem.tag] = sub_elem.text
            lista_produtos.append(obj)
        return lista_produtos
