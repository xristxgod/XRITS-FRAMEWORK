from typing import Optional, Dict
from urllib.parse import parse_qs


class Request:

    def __init__(self, environ: Dict, settings: Dict):
        self._build_get_prams_dict(environ["QUERY_STRING"])
        self._build_post_params_dict(environ["wsgi.input"].read())
        self.environ = environ
        self.settings = settings
        self.extra = {}

    def __getattr__(self, item):
        return self.extra.get(item)

    def _build_get_prams_dict(self, raw_params: str) -> Optional:
        self.GET = parse_qs(raw_params)

    def _build_post_params_dict(self, raw_bytes: bytes) -> Optional:
        raw_params = raw_bytes.decode("utf-8")
        self.POST = parse_qs(raw_params)


__all__ = [
    "Request"
]
