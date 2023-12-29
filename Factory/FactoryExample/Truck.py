from Factory.FactoryExample.Logistic import Logistic


class Truck(Logistic):
    def deliver(self):
        # Overriding the base class here and adding the message
        print("In Truck delivery mechanism..")