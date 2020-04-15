from Factory.ConcreteProduct2 import ConcreteProduct2
from Factory.Creator import Creator


class ConcreteCreator2(Creator):
    def factory(self) -> ConcreteProduct2:
        return ConcreteProduct2()
