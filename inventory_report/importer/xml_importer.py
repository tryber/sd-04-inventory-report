from inventory_report.importer.importer import Importer
from xml.etree.ElementTree import parse


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            data = []
            root = parse(file).getroot()
            for i in root:
                item = {}
                for pars in i:
                    item[pars.tag] = pars.text
                data.append(item)
            return data
