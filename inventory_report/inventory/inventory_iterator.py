from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_data = self.data[self.idx]
        except IndexError:
            self.idx = 0
            raise StopIteration
        else:
            self.idx += 1
            return next_data
