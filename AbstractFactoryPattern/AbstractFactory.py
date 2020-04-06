from abc import ABC, abstractmethod

from AbstractFactoryPattern import AbstractProductA, AbstractProductB


class AbstractFactory:
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
