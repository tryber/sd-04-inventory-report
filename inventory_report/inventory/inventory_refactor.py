from collections.abc import Iterable
from inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, path):
        self.data_inventory = []
        self.path = path

    def __iter__(self):
        return InventoryIterator(self.data_inventory)

    def import_data(self, pathfile, mode_report):
        self.data_inventory += self.path.import_data(pathfile)

        if mode_report == 'simples':
            return SimpleReport.generate(self.data_inventory)
        else:
            return CompleteReport.generate(self.data_inventory)
