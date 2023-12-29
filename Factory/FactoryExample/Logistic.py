# Interface is not suported by Python, use abstract classes instead
from abc import abstractmethod


class Logistic:
    @abstractmethod
    def deliver(self):
        # Method declared in abstract class will be overriden in base classes for their implementation
        pass
