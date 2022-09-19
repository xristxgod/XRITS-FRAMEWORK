import uuid
import urllib.parse

from src.Xrist.request import Request
from src import Response
from .base import BaseMiddleware


class Session(BaseMiddleware):
    def to_request(self, request: Request):
        cookie = request.environ.get("HTTP_COOKIE", None)
        if not cookie:
            return
        session_id = urllib.parse.parse_qs(cookie)["session_id"][0]
        request.extra['session_id'] = session_id

    def to_response(self, response: Response):
        if not response.request.settings_id:
            response.update_headers({"Set-Cookie": f"session_id={uuid.uuid4()}"})


__all__ = [
    "Session"
]
