from snail import BaseView, Request, Response


class HomepageView(BaseView):

    def get(self, request, *args, **kwargs) -> Response:
        return Response(body="Hello world")


class EpicMathView(BaseView):

    def get(self, request: Request, *args, **kwargs) -> Response:
        first = request.GET('first')
        return Response(body=f"{first}")
