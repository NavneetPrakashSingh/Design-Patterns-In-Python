from Builder.BuilderPattern.Product import Product
from Builder.BuilderPattern.Builder import Builder


class ConcreteBuilder(Builder):
    _product = Product()

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    def product(self) -> Product:
        return self._product

    def produce_part_a(self) -> None:
        self._product.add("Product_part_a")

    def produce_part_b(self) -> None:
        self._product.add("Product_part_b")
