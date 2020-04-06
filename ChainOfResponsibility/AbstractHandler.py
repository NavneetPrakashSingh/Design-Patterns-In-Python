from abc import abstractmethod
from typing import Optional

from ChainOfResponsibility.Handler import Handler


class AbstractHandler(Handler):
    _next_handler: Handler = None

    @abstractmethod
    def handle(self, request) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
