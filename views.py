from snail import BaseView


class HomepageView(BaseView):

    def get(self, request, *args, **kwargs):
        return "Hello world"
