from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, pathfile, mode_report):
        self.data += self.importer.import_data(pathfile)

        if mode_report == 'simples':
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)
