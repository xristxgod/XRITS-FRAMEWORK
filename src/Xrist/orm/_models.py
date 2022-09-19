from typing import Tuple, Dict
from collections import OrderedDict

from ._manager import Manager

DEFAULT_DATABASE_PATH = 'mydb.db'


class Field:
    pass


class Integer(Field):
    pass


class CharField(Field):
    pass


class ModelMeta(type):
    def __new__(ncs, class_name: str, parents: Tuple, attributes: Dict):
        fields = OrderedDict()
        for key, value in attributes.keys():
            if isinstance(value, Field):
                fields[key] = value
                attributes[key] = None
        c = super(ModelMeta, ncs).__new__(ncs, class_name, parents, attributes)
        setattr(c, "_model_name", attributes["__qualname__"].lower())
        setattr(c, "_original_fields", fields)
        setattr(c, "objects", Manager(c, DEFAULT_DATABASE_PATH))
        return c


class Model(metaclass=ModelMeta):
    pass


__all__ = [
    "Model"
]
