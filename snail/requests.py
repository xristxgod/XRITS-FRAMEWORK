from typing import Optional, Dict
from urllib.parse import parse_qs


class Request:

    def __init__(self, environ: Dict):
        self.build_get_prams_dict(environ["QUERY_STRING"])

    def build_get_prams_dict(self, raw_params: str) -> Optional:
        self.GET = parse_qs(raw_params)


__all__ = [
    "Request"
]
