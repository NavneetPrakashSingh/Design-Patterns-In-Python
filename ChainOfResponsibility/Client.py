from ChainOfResponsibility.DogHandler import DogHandler
from ChainOfResponsibility.Handler import Handler
from ChainOfResponsibility.MonkeyHandler import MonkeyHandler
from ChainOfResponsibility.SquirrelHandler import SquirrelHandler


def client_code(handler:Handler):
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    dog = DogHandler()
    squirrel = SquirrelHandler()

    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
