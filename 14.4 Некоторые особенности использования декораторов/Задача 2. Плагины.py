from typing import Callable

PLUGINS = dict()

def register(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func


@register
def hello(name):
    print('Hello {}!'.format(name))

print(PLUGINS)
hello('Артём')