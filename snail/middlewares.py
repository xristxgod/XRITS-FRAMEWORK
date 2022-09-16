from .requests import Request
from .responses import Response


class BaseMiddleware:
    def to_request(self, request: Request):
        return

    def to_response(self, response: Response):
        return