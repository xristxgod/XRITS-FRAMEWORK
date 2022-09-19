# from snail import Url
#
# from views import HomepageView
# from views import EpicMathView
#
#
# urlpatterns = [
#     Url("^$", HomepageView),
#     Url("^/math$", HomepageView),
# ]

class Test:
    def test(self):
        return "ga"


t = Test



d = getattr(t, "test")
print(d(t))