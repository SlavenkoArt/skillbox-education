new_line = input('Строка: ')

for index, sym in enumerate(new_line):
    if sym == '~':
        print(index, end=' ')