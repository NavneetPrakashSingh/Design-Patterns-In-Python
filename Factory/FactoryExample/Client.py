from Factory.FactoryExample.Ship import Ship
from Factory.FactoryExample.Truck import Truck


class Client:
    def invoke(self, transportation):
        # No if..else required, simply invoking the deliver gives us the concreate method. Leave it up to client to figure out what transportation to invoke.
        transportation.deliver()


client = Client()
client.invoke(Truck())
client.invoke(Ship())
