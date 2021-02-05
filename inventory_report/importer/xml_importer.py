import xmltodict
import json
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('.xml'):
            with open(path_file) as path_xml:
                data_xml = path_xml.read()
                xml_dict = xmltodict.parse(data_xml)
                data_json = json.dumps(xml_dict["dataset"]["record"])
                data_file = json.loads(data_json)
                return data_file
        else:
            return ValueError('Arquivo inválido')    
