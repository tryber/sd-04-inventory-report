from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

class Inventory:
    @classmethod
    def import_data(cls, filepath, report_type):
        ''' leitura de arquivos'''
        info = cls.import_products(filepath)
        return cls.generate_report(info, report_type)

    @classmethod
    def import_products(cls, filepath):
        '''Chama o metodo import_data das classes de acordo com o parametro recebido'''
        if filepath.endswith(".csv"):
            return CsvImporter.import_data(filepath)
        elif filepath.endswith(".json"):
            return JsonImporter.import_data(filepath)
        elif filepath.endswith(".xml"):
            return XmlImporter.import_data(filepath)

    @classmethod
    def generate_report(cls, lista_produtos, report_type):
        '''Chama o metodo generate de acordo com o parametro'''
        if report_type == "completo":
            return CompleteReport.generate(lista_produtos)
        else:
            return SimpleReport.generate(lista_produtos)
