from AbstractFactoryPattern.AbstractFactory import AbstractFactory
from AbstractFactoryPattern.ConcreteFactory1 import ConcreteFactory1
from AbstractFactoryPattern.ConcreteFactory2 import ConcreteFactory2


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.useful_method_a())
    print(product_b.useful_method_b())


if __name__ == "__main__":
    print("Testing code with concrete factory1")
    client_code(ConcreteFactory1())
    print("Testing code with concrete factory2")
    client_code(ConcreteFactory2())
