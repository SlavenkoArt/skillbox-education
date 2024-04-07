import builtins

global_count = {}


def decorator_counter(func):
    locale_count = {}

    def wrapped_func(*args, **kwargs):
        global global_count
        nonlocal locale_count
        global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
        locale_count[func.__name__] = locale_count.get(func.__name__, 0) + 1
        print(global_count, locale_count)
        print('*' * 100, '\n', dir(builtins))
        return func(*args, **kwargs)

    return wrapped_func()


@decorator_counter
def hello():
    print('hello')


@decorator_counter
def hello_2():
    print('hello')



print('*' * 100)
print(dir(__builtins__))
