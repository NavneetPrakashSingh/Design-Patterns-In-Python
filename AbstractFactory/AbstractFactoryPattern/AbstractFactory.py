from abc import abstractmethod

from AbstractFactory.AbstractFactoryPattern import AbstractProductA, AbstractProductB


class AbstractFactory:
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
