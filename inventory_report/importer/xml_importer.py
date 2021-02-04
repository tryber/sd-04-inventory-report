from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, pathname):
        if not pathname.endswith(".xml"):
            raise ValueError("Formato invalido")
        with open(pathname) as file:
            tree = ET.parse(file)
            root = tree.getroot()

            report = []

            for children in root:
                obj = {}
                for child in children:
                    obj[child.tag] = child.text
                    if obj not in report:
                        report.append(obj)

        return report


# XmlImporter.import_data('inventory_report/data/inventory.xml')
