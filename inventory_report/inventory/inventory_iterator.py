from collections.abc import Iterator


class InventoryInterator(Iterator):
    def __init__(self, datasource):
        self.datasource = datasource

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            next_item = self.datasource[self.index]
        except IndexError:
            raise StopIteration()
        else:
            self.index += 1
            return next_item
