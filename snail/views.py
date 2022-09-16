from .requests import Request
from .response import *


class BaseView:

    def get(self, request: Request, *args, **kwargs):
        pass

    def post(self, request: Request, *args, **kwargs):
        pass


__all__ = [
    "BaseView"
]
