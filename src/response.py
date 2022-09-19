from typing import Optional, Dict, Tuple

from .request import Request


class _Headers:
    __BASE_HANDLERS = {
        "Content-Type": "text/plain; charset=utf-8",
        "Content-Length": 0
    }

    def __init__(self, headers: Optional[Dict] = None):
        self._headers = self.__BASE_HANDLERS
        if headers is not None:
            self._headers.update(headers)

    @property
    def headers(self) -> Dict:
        return self._headers

    def update(self, value: Dict):
        self._headers.update(value)


class _Body:
    def __init__(self, raw_body: str = ''):
        self.__body = raw_body.encode("utf-8")

    @property
    def body(self) -> bytes:
        return self.__body


class Response:

    def __init__(self, request: Request, *, status_code: int = 200, headers: Optional[Dict] = None, body: str = ''):
        self._status_code = status_code
        self._headers = _Headers(headers)
        self._body = _Body(body)
        self.headers.update({"Content-Length": str(len(self.body.body))})
        self.request = request
        self.extra = {}

    @property
    def headers(self) -> Dict:
        return self._headers.headers

    @property
    def status_code(self) -> int:
        return self.status_code

    @property
    def body(self):
        return self._body.body

    def __getattr__(self, item):
        return self.extra.get(item)


__all__ = [
    "Response"
]
