from datetime import datetime

from snail import BaseView, Request, Response, build_template


class HomepageView(BaseView):

    def get(self, request, *args, **kwargs) -> Response:
        return Response(
            request,
            body=build_template(
                request,
                {"time": str(datetime.now())},
                "home.html"
            )
        )
