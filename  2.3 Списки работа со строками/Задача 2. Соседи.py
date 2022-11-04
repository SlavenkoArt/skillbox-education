S = input('Введите строку: ')
sym_number = int(input('Номер символа: '))
sym_list = list(S)
count = 0
left = ''
right = ''
sym_count = []

for i in sym_list:
    count += 1
    sym_count.append(i)
    if count == (sym_number - 1):
        left = i
    elif count == sym_number + 1:
        right = i

print('Символ слева: ', left)
print('Символ справа: ', right)


if sym_count[sym_number] == left and sym_count[sym_number] == right:
    print('Есть два таких же символа.')
elif sym_count[sym_number - 1] == left or sym_count[sym_number - 1] == right:
    print('Есть ровно один такой же символ.')
else:
    print('Таких же символов нет.')