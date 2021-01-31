from inventory_report.inventory.inventory_iterator import InventoryIterator
from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET
from collections.abc import Iterable
from ..importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator

Report = {"simples": SimpleReport, "completo": CompleteReport}


class InventoryRefactor(Iterable):
    def __init__(self, Importer):
        self.data = []
        self.importer = Importer

    def import_data(self, path, report_type):
        self.data += self.importer.import_data(path)
        return Report[report_type].generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
