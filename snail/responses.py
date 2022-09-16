from typing import Optional, Dict

from .requests import Request


class Response:

    def __init__(self, request: Request, status_code: int = 200, headers: Dict = None, body: str = ''):
        self.status_code = status_code
        self.headers = {}
        self.body = b''
        self._set_base_headers()
        if headers is not None:
            self.update_headers(headers)
        self._set_body(body)
        self.request = request
        self.extra = {}

    def __getattr__(self, item):
        return self.extra.get(item)

    def _set_base_headers(self) -> Optional:
        self.headers = {
            "Content-Type": "text/plain; charset=utf-8",
            "Content-Length": 0
        }

    def _set_body(self, raw_body: str) -> Optional:
        self.body = raw_body.encode("utf-8")
        self.update_headers({"Content-Length": str(len(self.body))})

    def update_headers(self, headers: Dict) -> Optional:
        self.headers.update(headers)


__all__ = [
    "Response"
]
