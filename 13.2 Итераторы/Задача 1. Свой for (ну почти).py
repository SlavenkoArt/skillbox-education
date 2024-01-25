new_list = [1, 2, 3, 4, 5, 6, 7]
iterator = iter(new_list)

while True:
    try:
        print(next(iterator))
    except Exception:
        print('Список пуст')
        break