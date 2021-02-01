from inventory_report.importer.importer import Importer
import xml


class XmlImporter(Importer):
    def import_data(pathname):
        if pathname.endswith(".xml"):
            values = []
            newXml = xml.etree.ElementTree.parse(pathname).getroot()
            for elem in newXml:
                obj = {}
                for subelem in elem:
                    obj[subelem.tag] = subelem.text
                values.append(obj)
            return values
        else:
            raise ValueError("Arquivo inválido")
