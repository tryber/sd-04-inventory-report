from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, info):
        self.info = info
        self._position = 0

    def __next__(self):
        try:
            value = self.info[self._position]
        except IndexError:
            raise StopIteration()
        else:
            self._position = self._position + 1
            return value
