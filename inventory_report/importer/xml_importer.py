from inventory_report.importer.importer import Importer
import xml


class XmlImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(filepath, encoding="utf-8") as file:
            data = []
            root = xml.etree.ElementTree.parse(file).getroot()
            for item in root:
                product = {}
                for parc in item:
                    product[parc.tag] = parc.text
                data.append(product)
            return data
