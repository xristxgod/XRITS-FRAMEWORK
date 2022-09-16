import re
from typing import Type, List, Dict, Callable

from .urls import Url
from .views import BaseView
from .requests import Request
from .exceptions import NotFound, NotAllowed
from .utils import Utils


class SnailRequestToResponse:
    @staticmethod
    def get_request(environ: Dict) -> Request:
        return Request(environ)

    @staticmethod
    def get_response(environ: Dict, view: BaseView, request: Request):
        method: str = environ["REQUEST_METHOD"].lower()
        if not hasattr(view, method):
            raise NotAllowed
        return getattr(view, method)(request)


class Snail:

    __slots__ = (
        "urls",
    )

    def __init__(self, urls: List[Url]):
        self.urls = urls

    def __call__(self, environ: Dict, start_response: Callable):
        view = self._get_view(environ)
        request = SnailRequestToResponse.get_request(environ)
        raw_response = SnailRequestToResponse.get_response(environ, view, request)
        response = raw_response.encode("utf-8")
        start_response(
            "200 OK",
            {"Content-Type": "text/plain; charset=utf-8"},
            {"Content-Length": str(len(response))}
        )
        return iter([response])

    def _find_view(self, raw_url: str) -> Type[BaseView]:
        url = Utils.prepare_url(raw_url)
        for path in self.urls:
            match = re.match(path.url, url)
            if match is not None:
                return path.view
        else:
            raise NotFound

    def _get_view(self, environ: Dict) -> BaseView:
        raw_url: str = environ["PATH_INFO"]
        view = self._find_view(raw_url)
        return view





__all__ = [
    "Snail"
]
