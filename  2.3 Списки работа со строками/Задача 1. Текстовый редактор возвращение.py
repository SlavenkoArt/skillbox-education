S = input('Введите строку: ')
S_list = list(S)
cor_list = []

for i in S:
    if i == ':':
        i = ';'
        cor_list.append(i)
    else:
        cor_list.append(i)

for i in cor_list:
    print(i, end='')
