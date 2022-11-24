def count(list):
    sym = 0
    for i in list:
        if i == '!' or '?':
            sym += 1
    return sym

first_list = []
second_list = []

question = input('Первое сообщение: ')
first_list = list(question)
question = input('Второе сообщение: ')
second_list = list(question)

if count(first_list) > count(second_list):
    first_list.extend(second_list)
    for i in first_list:
        print(i, end='')
if count(first_list) < count(second_list):
    second_list.extend(first_list)
    for i in second_list:
        print(i, end='')
if count(first_list) == count(second_list):
    print('Ой!')