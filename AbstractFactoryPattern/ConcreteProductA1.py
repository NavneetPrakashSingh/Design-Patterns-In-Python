from abc import ABC

from AbstractFactoryPattern.AbstractProductA import AbstractProductA


class ConcreteProductA1(AbstractProductA):
    def useful_method_a(self) -> str:
        return "Concrete Product A1 is called here"
