from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, source_path):
        if not source_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        # Opening JSON file
        data = ET.parse(source_path).getroot()

        # Convert dict to list
        product_list = []

        for row in data:
            formatted_row = {}
            for item in row:
                formatted_row[item.tag] = item.text

            product_list.append(formatted_row)

            return product_list
