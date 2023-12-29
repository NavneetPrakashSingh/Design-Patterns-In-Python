from Factory.FactoryPattern.Product import Product


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Operation from concrete product 1"
