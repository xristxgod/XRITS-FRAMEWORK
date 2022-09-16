import re
from typing import Type, List, Dict, Callable

from .urls import Url
from .views import BaseView
from .requests import Request
from .responses import Response
from .exceptions import NotFound, NotAllowed
from .utils import Utils


class SnailRequestToResponse:
    @staticmethod
    def get_request(environ: Dict, settings: Dict) -> Request:
        return Request(environ, settings=settings)

    @staticmethod
    def get_response(environ: Dict, view: BaseView, request: Request) -> Response:
        method: str = environ["REQUEST_METHOD"].lower()
        if not hasattr(view, method):
            raise NotAllowed
        return getattr(view, method)(request)


class Snail:

    __slots__ = (
        "urls", "settings"
    )

    def __init__(self, urls: List[Url], settings: Dict):
        self.urls = urls
        self.settings = settings

    def __call__(self, environ: Dict, start_response: Type[Callable]):
        view = self._get_view(environ)
        request = SnailRequestToResponse.get_request(environ, self.settings)
        response = SnailRequestToResponse.get_response(environ, view, request)
        start_response(str(response.status_code), response.headers.items())
        return iter([response.body])

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
