from collections.abc import Iterator


class InventoryItarator(Iterator):
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __next__(self):
        try:
            current_value = self._iterable[self._position]
        except IndexError:
            raise StopIteration()
        else:
            self._position += 1
            return current_value
