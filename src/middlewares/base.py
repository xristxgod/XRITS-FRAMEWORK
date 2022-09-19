from typing import Optional

from ..request import Request
from ..response import Response


class BaseMiddleware:
    def to_request(self, request: Request) -> Optional:
        pass

    def to_response(self, response: Response) -> Optional:
        pass


__all__ = [
    "BaseMiddleware"
]
