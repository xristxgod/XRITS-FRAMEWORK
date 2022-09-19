from ._query import Query
from ._connector import DBConnector


class Manager:
    def __init__(self, model_class, database_path: str):
        self.model_class = model_class
        self._model_fields = model_class._original_fields.keys()
        q = Query()
        self.q = q.SELECT(*self._model_fields).FROM(model_class._model_name)
        self._connector = DBConnector(database_path)

    def filter(self, *args, **kwargs) -> 'Manager':
        self.q = self.q.WHERE(*args, **kwargs)
        return self

    def fetch(self):
        q = str(self.q)
        db_result = self._connector.fetch(q)
        results = []
        for row in db_result:
            model = self.model_class()
            for field, value in zip(self._model_fields, row):
                setattr(model, field, value)
            results.append(model)
        return results


__all__ = [
    "Manager"
]
