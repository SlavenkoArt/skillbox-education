import time
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        run_time = stop - start
        return '{} секунд'.format(run_time)
    return wrapped_func


@timer
def function():
    return [x ** 2 ** 2 for x in range(50)]


my_timer = function()
print(my_timer)
