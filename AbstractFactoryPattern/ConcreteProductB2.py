from AbstractFactoryPattern.AbstractProductB import AbstractProductB


class ConcreteProductB2(AbstractProductB):
    def useful_method_b(self) -> str:
        return "This one is from concrete product b2"
