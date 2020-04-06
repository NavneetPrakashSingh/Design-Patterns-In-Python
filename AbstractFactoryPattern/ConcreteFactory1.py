from AbstractFactoryPattern import AbstractProductB
from AbstractFactoryPattern.ConcreteProductA1 import ConcreteProductA1
from AbstractFactoryPattern.AbstractFactory import AbstractFactory
from AbstractFactoryPattern.ConcreteProductB1 import ConcreteProductB1


class ConcreteFactory1(AbstractFactory):

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()
