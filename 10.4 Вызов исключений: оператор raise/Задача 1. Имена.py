sym_sum = 0
count = 0

try:
    text = open('people.txt', 'r', encoding='utf-8')
    for sym in text:
        count += 1
        leingh = len(sym)
        if sym.endswith('\n'):
            leingh -= 1
            if len(sym) - 1 < 3:
                raise BaseException('Длина {} строки меньше трёх символов'.format(count))
        sym_sum += leingh
except FileNotFoundError:
    print('Файл не найден.')
finally:
    print('Найденная сумма символов ', sym_sum)
