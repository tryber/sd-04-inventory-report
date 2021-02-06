from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self.position = 0
        self.iterable = iterable

    def __next__(self):
        try:
            iteration = self.iterable[self.position]
        except IndexError:
            raise StopIteration()
        else:
            self.position += 1
            return iteration
