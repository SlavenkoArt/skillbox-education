line = input('Введите строку: ')

lowers = len([sym for sym in line if sym.islower()])
uppers = len([sym for sym in line if sym.isupper()])

if lowers > uppers:
    print('Результат: ', line.lower())
else:
    print('Результат: ', line.upper())