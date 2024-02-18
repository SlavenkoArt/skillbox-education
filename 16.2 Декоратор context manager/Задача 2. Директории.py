from contextlib import contextmanager
import os


@contextmanager
def in_dir(path):
    cur_path = os.getcwd()
    try:
        yield
        os.chdir(path)
    except FileNotFoundError:
        print('Путь не существует')
    finally:
        os.chdir(cur_path)
        print(f'Возвращаемся в прежнюю директорию {cur_path}')


with in_dir('/Users/Sharedd'):
    print(os.listdir())
