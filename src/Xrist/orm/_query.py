class Query:
    def __init__(self):
        self._data = {
            "select": [],
            "from": []
        }

    def SELECT(self, *args):
        self._data["select"].extend(args)

    def FROM(self, *args):
        self._data["from"].extend(args)

    def _line(self, key):
        separator = ","
        return separator.join(self._data[key])

    def _lines(self):
        for key in self._data.keys():
            yield key.upper() + '\n'
            yield '\t' + self._line(key) + '\n'

    def __str__(self):
        return "".join(self._lines())

