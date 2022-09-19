from typing import Type
from dataclasses import dataclass

from .views import BaseView


@dataclass()
class Url:
    url: str
    view: Type[BaseView]


__all__ = [
    "Url"
]
