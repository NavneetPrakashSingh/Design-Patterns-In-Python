from ChainOfResponsibility.AbstractHandler import AbstractHandler


class DogHandler(AbstractHandler):
    def handle(self, request) -> str:
        if request == "MeatBall":
            return "Dog: I'll eat the {request}"
        else:
            return super().handle(request)
