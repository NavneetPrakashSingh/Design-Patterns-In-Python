from AbstractFactory.AbstractFactoryPattern.AbstractProductB import AbstractProductB


class ConcreteProductB1(AbstractProductB):
    def useful_method_b(self) -> str:
        return "This one is from Concrete Product B1"
