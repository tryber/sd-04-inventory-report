from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self.iterable = iterable
        self.initial_position = 0

    def __next__(self):
        try:
            interation_value = self.iterable[self.initial_position]
        except IndexError:
            raise StopIteration()
        else:
            self.initial_position += 1
            return interation_value
