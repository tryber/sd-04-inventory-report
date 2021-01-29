from collections.abc import Iterator

class InventoryIterator (Iterator):
    def __init__ (self, data):
        self.data = data

    def __next__ (self):
        print('ola')
        for element in self.data:
            yield element
