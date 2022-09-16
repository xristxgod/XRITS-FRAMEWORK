from .requests import Request
from .responses import Response


class BaseView:

    def get(self, request: Request, *args, **kwargs) -> Response:
        pass

    def post(self, request: Request, *args, **kwargs) -> Response:
        pass


__all__ = [
    "BaseView"
]
