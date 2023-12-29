class Product:
    _list = []

    def __init__(self):
        self._list = []

    def add(self, part) -> None:
        self._list.append(part)

    def print_list(self) -> None:
        print(self._list)
