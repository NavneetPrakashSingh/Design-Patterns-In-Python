from Factory.ConcreteProduct1 import ConcreteProduct1
from Factory.Creator import Creator


class ConcreteCreator1(Creator):
    def factory(self) -> ConcreteProduct1:
        return ConcreteProduct1()
