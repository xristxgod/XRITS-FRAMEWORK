from typing import Any, Optional, Generator


AND = "AND"
OR = "OR"


class Q:

    def __init__(self, exp_type: str = AND, **kwargs):
        self.separator = exp_type
        self._params = kwargs

    def __str__(self):
        return f" {self.separator} ".join([f"{key} = {value}" for key, value in self._params.items()])

    def __bool__(self):
        return bool(self._params)


class BaseExp:
    name = None

    def add(self, *args, **kwargs):
        raise NotImplementedError()

    def definition(self) -> str:
        return self.name + "\n\t" + self.line() + '\n'

    def line(self) -> str:
        raise NotImplementedError()

    def __bool__(self):
        raise NotImplementedError()


class _Select(BaseExp):
    name = "SELECT"

    def __init__(self):
        self._params = []

    def add(self, *args, **kwargs) -> Optional:
        self._params.extend(args)

    def line(self) -> str:
        separator = ","
        return separator.join(self._params)

    def __bool__(self):
        return bool(self._params)


class _From(BaseExp):
    name = "FROM"

    def __init__(self):
        self._params = []

    def add(self, *args, **kwargs) -> Optional:
        self._params.extend(args)

    def line(self) -> str:
        separator = ","
        return separator.join(self._params)

    def __bool__(self):
        return bool(self._params)


class _Where(BaseExp):
    name = "WHERE"

    def __init__(self, exp_type: str = AND, **kwargs):
        self._q = Q(exp_type=exp_type, **kwargs)

    def add(self, exp_type: str = AND, **kwargs) -> 'Q':
        self._q = Q(exp_type, **kwargs)
        return self._q

    def line(self) -> str:
        return str(self._q)

    def __bool__(self):
        return bool(self._q)


class Query:
    def __init__(self):
        self._data = {
            "select": _Select(),
            "from": _From(),
            "where": _Where()
        }

    def SELECT(self, *args: str) -> 'Query':
        self._data["select"].add(*args)
        return self

    def FROM(self, *args: str) -> 'Query':
        self._data["from"].add(*args)
        return self

    def WHERE(self, exp_type: str = AND, **kwargs) -> 'Query':
        self._data["where"].add(exp_type, **kwargs)
        return self

    def _lines(self) -> Generator:
        for key, value in self._data.items():
            yield value.definition()

    def __str__(self):
        return "".join(self._lines())


__all__ = [
    "Query"
]

