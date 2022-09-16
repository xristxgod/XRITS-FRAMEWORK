from typing import Callable


class Snail:
    def __call__(self, environ, start_response: Callable):
        data = b"Hello world\n"
        start_response(
            "200 OK",
            {"Content-Type": "text/plain"},
            {"Content-Length": str(len(data))}
        )
        return iter([data])
