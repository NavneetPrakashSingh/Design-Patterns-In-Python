from Factory.FactoryExample.Logistic import Logistic


class Ship(Logistic):
    def deliver(self):
        # Overriding the base class here and adding the message
        print("In Ship delivery mechanism..")
