from abc import abstractmethod


class Creator:

    @abstractmethod
    def factory(self):
        pass

    def some_operation(self) -> str:
        product = self.factory()
        return product.operation()
