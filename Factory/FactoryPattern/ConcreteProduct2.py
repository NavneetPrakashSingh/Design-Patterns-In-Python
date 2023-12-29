from Factory.FactoryPattern.Product import Product


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Operation from concrete product 2"
