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

    def import_data(self, filepath, report_type):
        self.data += self.importer.import_data(filepath)
        result = []
        if report_type == "simples":
            result = SimpleReport.generate(self.data)
        elif report_type == "completo":
            result = CompleteReport.generate(self.data)
        return result
