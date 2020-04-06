from ChainOfResponsibility.AbstractHandler import AbstractHandler


class SquirrelHandler(AbstractHandler):
    def handle(self, request) -> str:
        if request == "Nut":
            return "Squirrel: I'll eat the nut"
        else:
            return super().handle(request)
