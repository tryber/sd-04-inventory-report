from collections.abc import Iterable
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.inventory.inventory import SimpleReport
from inventory_report.inventory.inventory import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path_file, tipo):
        self.data.extend(self.importer.import_data(path_file))
        if tipo == "simples":
            simple = SimpleReport.generate(self.data)
            return simple
        else:
            complete = CompleteReport.generate(self.data)
            return complete
