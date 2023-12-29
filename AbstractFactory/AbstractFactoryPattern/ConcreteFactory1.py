from AbstractFactory.AbstractFactoryPattern.ConcreteProductA1 import ConcreteProductA1
from AbstractFactory.AbstractFactoryPattern.AbstractFactory import AbstractFactory
from AbstractFactory.AbstractFactoryPattern.ConcreteProductB1 import ConcreteProductB1


class ConcreteFactory1(AbstractFactory):

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()
