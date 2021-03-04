from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryItarator

from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __inter__(self):
        return InventoryItarator(self.data)

    def import_data(self, path, tipo):
        self.data += self.importer.import_data(path)
        result = []
        if tipo == "simples":
            result = SimpleReport.generate(self.data)
        elif tipo == "completo":
            result = CompleteReport.generate(self.data)
        return result
