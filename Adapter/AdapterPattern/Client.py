from Adapter.AdapterPattern.Adaptee import Adaptee
from Adapter.AdapterPattern.Adapter import Adapter
from Adapter.AdapterPattern.Target import Target


def client_code(target: Target) -> None:
    print(target.request())


if __name__ == "__main__":
    print("Target class called")
    target = Target()
    client_code(target)

    print("Inside adaptee class which contains the reversed string")
    adaptee = Adaptee()
    print(adaptee.special_method())

    print("Adding adapter to the adaptee class to make it compatible")
    adapter = Adapter(adaptee)
    print(adapter.request())

