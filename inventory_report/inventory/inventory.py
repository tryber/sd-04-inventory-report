from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def simple_complete(cls, stock, tipe):
        if tipe == 'simples':
            return SimpleReport.generate(stock)
        else:
            return CompleteReport.generate(stock)

    @classmethod
    def import_data(cls, filepath, tipe):
        if filepath.endswith('.csv'):
            dado = CsvImporter.import_data(filepath)
            return cls.simple_complete(dado, tipe)
        elif filepath.endswith('.json'):
            dado = JsonImporter.import_data(filepath)
            return cls.simple_complete(dado, tipe)
        elif filepath.endswith('.xml'):
            dado = XmlImporter.import_data(filepath)
            return cls.simple_complete(dado, tipe)
# arg1 = 'inventory_report/data/inventory.csv'
# arg3 = 'inventory_report/data/inventory.json'
# arg2 = 'simples'
# arg4 = 'completo'
# tentando dar push

# def teste(caminho, tipo):
#     a = Inventory()
#     return a.import_data(caminho, tipo)


# print(teste(arg3, arg4))
