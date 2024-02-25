import time
from datetime import datetime


def createtime(cls):
    """Декоратор класса. Выводит время создания инстанса класса."""

    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print("Время создания инстанса класса: ", datetime.utcnow())
        print("Методы: ", end='')
        for i_method in dir(cls):
            if i_method.startswith('_'):
                continue
            print(i_method, end='')
        print('\n')

        return instance

    return wrapper


@createtime
class Example:
    def helo1(self):
        print('Hello world')

    def helo2(self):
        print('Hello Python')


Example()
time.sleep(1)
Example()