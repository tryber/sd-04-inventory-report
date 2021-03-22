from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator

from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, tipo):
        self.data += self.importer.import_data(path)
        if tipo == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)
