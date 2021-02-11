from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(filepath):
        if not filepath.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        with open(filepath) as xml_file:
            root = ET.parse(xml_file).getroot()
            records = root.findall('record')
            output = []
            for record in records:
                dictionary = {}
                for element in record:
                    dictionary[element.tag] = element.text
                output.append(dictionary)
            return output
