from collections.abc import Iterable
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator

classes = {"simples": SimpleReport, "completo": CompleteReport}

class InventoryRefactor(Iterable):

    def __init__ (self, Importer):
        self.data = []
        self.importer = Importer

    def import_data(self, path, report_type):
        self.data += self.importer.import_data(path)
        return classes[report_type].generate(self.data)

    def __iter__ (self):
        print(self.data)
        return InventoryIterator(self.data)

test = {
          'id': '1',
          'nome_do_produto': 'Nicotine Polacrilex',
          'nome_da_empresa': 'Target Corporation',
          'data_de_fabricacao': '2020-02-18',
          'data_de_validade': '2022-09-17',
          'numero_de_serie': 'CR25 1551 4467 2549 4402 1',
          'instrucoes_de_armazenamento': 'instrucao 1'
       }

instance = InventoryRefactor(XmlImporter)
instance.import_data('inventory_report/data/inventory.xml', 'simples')
iterator = iter(instance)
#first_item_instance = next(iterator)

#print(first_item_instance)

for test in iterator:
    print(test)