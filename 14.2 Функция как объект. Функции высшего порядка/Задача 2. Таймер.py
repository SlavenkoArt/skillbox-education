import time


def timer(func):
    start = time.time()
    func()
    stop = time.time()
    return f'{stop - start} секунд'


@timer
def function():
    return [x ** 2 ** x for x in range(20)]


print(function)
