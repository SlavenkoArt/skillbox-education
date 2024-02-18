import time
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as ex:
        print(ex)
    finally:
        print(time.time() - start)


with timer() as t1:
    print('Первая часть')
    val_1 = 100 * 1000 * 10000

with timer() as t2:
    print('Вторая часть')
    val_2 = 100 * 1000 * 50000

with timer() as t3:
    print('Третья часть')
    val_3 = 100 * 1000 * 100000
