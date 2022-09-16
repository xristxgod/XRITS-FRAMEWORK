from snail import BaseView, Request


class HomepageView(BaseView):

    def get(self, request, *args, **kwargs):
        return "Hello world"


class EpicMathView(BaseView):

    def get(self, request: Request, *args, **kwargs):
        first = request.GET('first')
        if not first or not first[0].isnumeric():
            return f"fsadfas"
