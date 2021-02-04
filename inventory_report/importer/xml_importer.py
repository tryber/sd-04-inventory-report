import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('.json'):
            path_xml = open(path_file)
            data_xml = path_xml.read()
            data_file = xmltodict.parse(data_xml)
            return data_file
