from typing import Callable, Any


def count_func(count: int) -> Callable:
    def do_twice(func: Callable) -> Callable:
        def input_file(*args, **kwargs) -> Any:
            for _ in range(count):
                func(*args, **kwargs)
            return
        return input_file
    return do_twice


@count_func(count=4)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Artem')
