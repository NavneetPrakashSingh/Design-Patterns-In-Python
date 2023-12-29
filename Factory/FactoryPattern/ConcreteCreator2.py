from Factory.FactoryPattern.ConcreteProduct2 import ConcreteProduct2
from Factory.FactoryPattern.Creator import Creator


class ConcreteCreator2(Creator):
    def factory(self) -> ConcreteProduct2:
        return ConcreteProduct2()
