import inspect
from typing import Tuple, Dict
from collections import OrderedDict

from ._manager import Manager
from .fields import BaseField


def _has_contribute_to_class(value):
    # Only call contribute_to_class() if it's bound.
    return not inspect.isclass(value) and hasattr(value, "contribute_to_class")


class ModelBase(type):
    def __new__(cls, class_name: str, bases: Tuple, attrs: Dict, **kwargs):
        # fields = OrderedDict()
        # for key, value in attributes.keys():
        #     if isinstance(value, BaseField):
        #         fields[key] = value
        #         attributes[key] = None
        # c = super(ModelBase, ncs).__new__(ncs, class_name, parents, attributes)
        # setattr(c, "_model_name", attributes["__qualname__"].lower())
        # setattr(c, "_original_fields", fields)
        # setattr(c, "objects", Manager(c, DEFAULT_DATABASE_PATH))
        # return c
        super_new = super().__new__
        parents = [base for base in bases if isinstance(base, ModelBase)]
        if not parents:
            return super_new(cls, class_name, bases, attrs)

        new_attrs = {"__module__": attrs.pop("__module__")}
        classcell = attrs.pop("__classcell__", None)
        if classcell is not None:
            new_attrs.update({"__classcell__": classcell})
        contributable_attrs = {}
        for object_name, _object in attrs.items():
            if _has_contribute_to_class(_object):
                contributable_attrs.update({object_name: _object})
            else:
                new_attrs.update({object_name: _object})
        new_class = super_new(cls, class_name, bases, attrs, **kwargs)
        attr_meta = attrs.pop("Meta", None)

        abstract = getattr(attr_meta, "abstract", False)
        meta = attr_meta or getattr(new_class, "Meta", None)
        base_meta = getattr(new_class, "_meta", None)

        


class Model(metaclass=ModelBase):
    pass


__all__ = [
    "Model"
]
