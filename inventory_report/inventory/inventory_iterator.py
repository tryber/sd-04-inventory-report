# https://www.programiz.com/python-programming/iterator
# https://www.w3schools.com/python/python_iterators.asp
# https://refactoring.guru/pt-br/design-patterns/iterator/python/example
from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self._position = 0

    def __next__(self):
        try:
            value = self.data[self._position]
        except IndexError:
            raise StopIteration()
        else:
            self._position += 1
            return value
