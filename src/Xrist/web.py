import re
from typing import Type, List, Dict, Callable

from .types import Url
from .request import Request
from .response import Response
from .views import BaseView
from .exceptions import NotFound, NotAllowed
from src.Xrist.middlewares import BaseMiddleware, DEFAULT_MIDDLEWARE


def __prepare_url(url: str):
    return url[:-1] if url[-1] == "/" else url


class _ViewController:
    @staticmethod
    def find_view(urls: List[Url], raw_url: str) -> Type[BaseView]:
        url = raw_url[:-1] if raw_url[-1] == "/" else raw_url
        for path in urls:
            match = re.match(path.url, url)
            if match is not None:
                return path.view
        else:
            raise NotFound


class _ReqResController:
    @staticmethod
    def get_request(environ: Dict, settings: Dict) -> Request:
        return Request(environ, settings=settings)

    @staticmethod
    def get_response(environ: Dict, view: Type[BaseView], request: Request) -> Response:
        method: str = environ["REQUEST_METHOD"].lower()
        if not hasattr(view, method):
            raise NotAllowed
        return getattr(view, method)(request)


class _MiddlewareController:
    @staticmethod
    def apply_middleware(method: str, middlewares: List[Type[BaseMiddleware]]):
        if method.lower() not in ["request", "response"]:
            raise ValueError
        for middleware in middlewares:
            getattr(middleware, f"to_{method}")(middleware)


class Application:
    __VIEW_CONTROLLER = _ViewController
    __REQ_RES_CONTROLLER = _ReqResController
    __MIDDLEWARE_CONTROLLER = _MiddlewareController

    __slots__ = (
        "instance", "urls", "settings", "middlewares"
    )

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(Application, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self, urls: List[Url], *, settings: Dict, middlewares: List[Type[BaseMiddleware]] = DEFAULT_MIDDLEWARE):
        self.urls = urls
        self.settings = settings
        self.middlewares = middlewares

    def __call__(self, environ: Dict, start_response: Type[Callable]):
        view = self.__VIEW_CONTROLLER.find_view(self.urls, environ["PATH_INFO"])
        request = self.__REQ_RES_CONTROLLER.get_request(environ, self.settings)
        self.__MIDDLEWARE_CONTROLLER.apply_middleware("request", self.middlewares)
        response = self.__REQ_RES_CONTROLLER.get_response(environ, view, request)
        self.__MIDDLEWARE_CONTROLLER.apply_middleware("response", self.middlewares)
        start_response(str(response.status_code), response.headers.items())
        return iter([response.body])


__all__ = [
    "Application"
]
