from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, rel_type):
        self.data = [*self.data, *self.importer.import_data(path)]
        if rel_type == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)


if __name__ == "__main__":
    print(
        InventoryRefactor.import_data(
            "inventory_report/data/inventory.csv", "simples"
        )
    )
    print(
        InventoryRefactor.import_data(
            "inventory_report/data/inventory.csv", "completo"
        )
    )
    print(
        InventoryRefactor.import_data(
            "inventory_report/data/inventory.json", "simples"
        )
    )
    print(
        InventoryRefactor.import_data(
            "inventory_report/data/inventory.json", "completo"
        )
    )
    print(
        InventoryRefactor.import_data(
            "inventory_report/data/inventory.xml", "simples"
        )
    )
    print(
        InventoryRefactor.import_data(
            "inventory_report/data/inventory.xml", "completo"
        )
    )

    inventory = InventoryRefactor()
    inventory.import_data("inventory_report/data/inventory.csv", "simples")
    iterator = iter(inventory)
    first_item = next(iterator)
    print(first_item)
