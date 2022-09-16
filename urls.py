from snail import Url

from views import HomepageView
from views import EpicMathView


urlpatterns = [
    Url("^$", HomepageView),
    Url("^/math$", HomepageView),
]