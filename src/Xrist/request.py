import urllib.parse
from typing import Optional, Union, Dict


def _get_raw_data_to_dict(raw_data: Union[str, bytes]) -> Optional[Dict]:
    if isinstance(raw_data, str):
        return urllib.parse.parse_qs(raw_data)
    elif isinstance(raw_data, bytes):
        return urllib.parse.parse_qs(raw_data.decode("utf-8"))
    else:
        return None


class HttpMethod:
    def __init__(self, name: str, *, data: Dict):
        self.name: str = name
        self.data: Dict = data

    @property
    def method(self):
        return self.data


class Request:
    def __init__(self, environ: Dict, settings: Dict):
        self.GET = HttpMethod("GET", data=_get_raw_data_to_dict(environ["QUERY_STRING"]))
        self.POST = HttpMethod("POST", data=_get_raw_data_to_dict(environ["wsgi.input"].read()))
        self._environ = environ
        self._settings = settings
        self.extra = {}

    def __getattr__(self, item):
        return self.extra.get(item)


__all__ = [
    "Request"
]
