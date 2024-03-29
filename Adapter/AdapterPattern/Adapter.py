from Adapter.AdapterPattern.Adaptee import Adaptee
from Adapter.AdapterPattern.Target import Target


class Adapter(Target):

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return self.adaptee.special_method()[::-1]
