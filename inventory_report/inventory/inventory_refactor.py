from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    @staticmethod
    def call_report(self, rep_type, output):
        if rep_type == 'simples':
            return(SimpleReport.generate(output))
        elif rep_type == 'completo':
            return(CompleteReport.generate(output))
        else:
            return('Opção inválida')

    def import_data(self, file_path, report_type):
        output = []
        output = self.importer.import_data(file_path)
        for item in output:
            self.data.append(dict(item))

        return InventoryRefactor.call_report(self, report_type, output)

    def __iter__(self):
        return InventoryIterator(self.data)
