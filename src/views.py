from .request import Request
from .response import Response


class BaseView:
    def get(self, request: Request, *args, **kwargs) -> Response:
        raise NotImplementedError

    def post(self, request: Request, *args, **kwargs) -> Response:
        raise NotImplementedError
