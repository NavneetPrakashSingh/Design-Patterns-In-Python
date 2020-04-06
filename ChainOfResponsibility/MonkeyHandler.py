from ChainOfResponsibility.AbstractHandler import AbstractHandler


class MonkeyHandler(AbstractHandler):
    def handle(self, request) -> str:
        if request == "Banana":
            return "Monkey: I'll eat the Banana"
        else:
            return super().handle(request)
