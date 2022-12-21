line = input('Введите строку: ')
symbol = input('Введите символ: ')

double_line = [i * 2 for i in list(line)]
line_symbol = [i + symbol for i in list(double_line)]

print('Список удвоенных символов: ', double_line)
print('Склейка с дополнительным символом ', line_symbol)