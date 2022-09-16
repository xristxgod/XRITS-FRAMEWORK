from snail import Snail
from urls import urlpatterns


def main():
    snail = Snail(
        urls=urlpatterns
    )


if __name__ == '__main__':
    main()
