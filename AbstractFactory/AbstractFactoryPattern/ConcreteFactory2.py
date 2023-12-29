from AbstractFactory.AbstractFactoryPattern.AbstractFactory import AbstractFactory
from AbstractFactory.AbstractFactoryPattern.ConcreteProductA2 import ConcreteProductA2
from AbstractFactory.AbstractFactoryPattern.ConcreteProductB2 import ConcreteProductB2


class ConcreteFactory2(AbstractFactory):
    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()
