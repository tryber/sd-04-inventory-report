from collections.abc import Iterator


class InventoryItarator(Iterator):
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __next__(self):
        try:
            current_value = self.data[self.position]
        except IndexError:
            raise StopIteration()
        else:
            self.position += 1
            return current_value
