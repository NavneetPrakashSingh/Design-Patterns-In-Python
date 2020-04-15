from Factory.ConcreteCreator1 import ConcreteCreator1
from Factory.ConcreteCreator2 import ConcreteCreator2
from Factory.Creator import Creator


def client(creator: Creator) -> None:
    print(creator.some_operation())


if __name__ == "__main__":
    client(ConcreteCreator1())
    client(ConcreteCreator2())
