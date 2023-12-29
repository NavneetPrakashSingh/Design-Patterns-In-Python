from AbstractFactory.AbstractFactoryPattern.AbstractProductA import AbstractProductA


class ConcreteProductA2(AbstractProductA):
    def useful_method_a(self) -> str:
        return "Concrete Product A2 is called here"

