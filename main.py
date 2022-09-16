import os

from snail import Snail
from urls import urlpatterns


settings = {
    "BASE_DIR": os.path.dirname(os.path.abspath(__file__)),
    "TEMPLATE_DIR_NAME": 'templates'
}


def main():
    snail = Snail(
        urls=urlpatterns,
        settings=settings
    )


if __name__ == '__main__':
    main()
