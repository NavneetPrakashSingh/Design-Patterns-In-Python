from __future__ import annotations

from abc import abstractmethod, ABC
from typing import Optional


class Handler(object):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass