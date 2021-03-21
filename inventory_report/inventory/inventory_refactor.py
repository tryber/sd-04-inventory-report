from collections.abc import Iterable

from inventory_report.inventory.inventory_iterator import InventoryInterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryInterator(self.data)

    def import_data(self, source_path, report_type):
        self.data += self.importer.import_data(source_path)

        return (SimpleReport, CompleteReport)[report_type == "simples"]
