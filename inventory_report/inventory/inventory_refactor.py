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

    def import_data(self, filepath, reporter_type):
        self.data = [*self.data, *self.importer.import_data(filepath)]
        return self.generate_report(self.data, reporter_type)

    @classmethod
    def generate_report(cls, products_list, reporter_type):
        if reporter_type == "simples":
            return SimpleReport.generate(products_list)
        else:
            return CompleteReport.generate(products_list)
