from typing import Optional

from src.Xrist.request import Request
from src import Response


class BaseMiddleware:
    def to_request(self, request: Request) -> Optional:
        pass

    def to_response(self, response: Response) -> Optional:
        pass


__all__ = [
    "BaseMiddleware"
]
