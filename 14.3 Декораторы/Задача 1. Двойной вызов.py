from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    def input_file(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return input_file


def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Artem')
