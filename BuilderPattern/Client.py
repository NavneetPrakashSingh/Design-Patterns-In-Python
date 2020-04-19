from BuilderPattern.ConcreteBuilder import ConcreteBuilder
from BuilderPattern.Director import Director


def client():
    builder = ConcreteBuilder()
    director = Director()
    director.builder(builder)

    print("Free version")
    director.build_free_version()
    builder.product().print_list()

    builder.reset()
    print("Paid Version")
    director.build_paid_version()
    builder.product().print_list()


if __name__ == "__main__":
    client()
