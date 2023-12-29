from Builder.BuilderPattern.Builder import Builder


class Director:
    _builder = Builder()

    def __init__(self):
        self._builder = Builder()

    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_free_version(self) -> None:
        self._builder.produce_part_a()

    def build_paid_version(self) -> None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
