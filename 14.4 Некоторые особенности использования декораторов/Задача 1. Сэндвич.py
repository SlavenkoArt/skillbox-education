def buns(func):
    def wrapped_func(*args, **kwargs):
        print(' <------->')
        func(*args, **kwargs)
        print(' <_______>')
    return wrapped_func

def ingredients(func):
    def wrapped_func(*args, **kwargs):
        print(' #помидор#')
        func(*args, **kwargs)
        print('  -салат-')
        func(' ~~соус~~')
    return wrapped_func

@buns
@ingredients
def ham(name):
    print(name)

ham('--ветчина--')