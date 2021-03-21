from collections.abc import Iterator


class InventoryInterator(Iterator):
    def __init__(self, datasource):
        self.datasource = datasource
        self.actualIndex = 0

    def __next__(self):
        try:
            next_item = self.datasource[self.actualIndex]
        except IndexError:
            raise StopIteration()
        else:
            self.actualIndex += 1
            return next_item
