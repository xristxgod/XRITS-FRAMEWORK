from datetime import datetime

from snail import BaseView, Request, Response, build_template


class HomepageView(BaseView):

    def get(self, request, *args, **kwargs) -> Response:
        return Response(
            body=build_template(
                request,
                {"time": str(datetime.now())},
                "home.html"
            )
        )


class EpicMathView(BaseView):

    def get(self, request: Request, *args, **kwargs) -> Response:
        first = request.GET('first')
        return Response(body=f"{first}")
