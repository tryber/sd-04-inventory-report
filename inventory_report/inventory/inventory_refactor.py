from collections.abc import Iterable
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
from .inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def import_data(self, path, report_type):
        self.data += self.importer.import_data(path)
        return (
            SimpleReport.generate(self.data)
            if report_type == "simples"
            else CompleteReport(self.data)
        )

    def __iter__(self):
        return InventoryIterator(self.data)
