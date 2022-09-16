from typing import Dict

from .requests import Request


class Utils:
    @staticmethod
    def prepare_url(url: str):
        if url[-1] == "/":
            return url[:-1]
        return url


__all__ = [
    "Utils"
]
