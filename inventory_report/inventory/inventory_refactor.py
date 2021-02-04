from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, Importer):
        self.data = []
        self.importer = Importer

    def import_data(self, data_path, report_type):
        self.data += self.importer.import_data(data_path)
        if report_type == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
