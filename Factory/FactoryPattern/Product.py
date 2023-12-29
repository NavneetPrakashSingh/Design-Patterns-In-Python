from abc import abstractmethod


class Product:
    @abstractmethod
    def operation(self) -> str:
        pass
