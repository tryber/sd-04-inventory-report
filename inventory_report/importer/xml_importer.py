from inventory_report.importer.importer import Importer
from xml.etree import ElementTree


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith('.xml'):
            root = ElementTree.parse(file_name).getroot()
            records = root.findall("record")
            records_list = []
            for elem in records:
                temp_dict = {}
                for e in elem:
                    temp_dict[e.tag] = e.text
                records_list.append(temp_dict)
            return records_list

        else:
            raise ValueError("Arquivo inválido")


if __name__ == "__main__":
    print(XmlImporter.import_data('inventory_report/data/inventory.xml'))
