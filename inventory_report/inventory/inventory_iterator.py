from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self.iterable = iterable
        self.position = 0

    def __next__(self):
        try:
            current_value = self.iterable[self.position]
        except IndexError:
            raise StopIteration()
        else:
            self.position += 1
            return current_value
