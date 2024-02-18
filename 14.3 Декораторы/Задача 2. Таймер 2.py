import time
from typing import Callable, Any


def sleep(sleep_time: int) -> Callable:
    def timer(func: Callable) -> Callable:
        def wrapped_func(*args, **kwargs) -> Any:
            print(f'Начнем через {sleep_time}')
            time.sleep(sleep_time)
            start = time.time()
            func(*args, **kwargs)
            stop = time.time()
            run_time = stop - start
            return '{} секунд'.format(run_time)
        return wrapped_func
    return timer


@sleep(3)
def function():
    return [x ** 2 ** 2 for x in range(50)]


my_timer = function()
print(my_timer)
