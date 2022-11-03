N = int(input('Количество чисел в списке: '))
list_num = []
count = 0
index_sum = 0
index_num = []

for _ in range(N):
    print('Введите', _ + 1, 'число:', end=' ')
    num = int(input())
    list_num.append(num)

divider = int(input('Введите делитель: '))

for number in list_num:
    if number % divider == 0:
        index_num.append(number)

for symbol in index_num:
    count += 1
    print('Индекс числа ', symbol, ': ', count)
    index_sum += count

print('Сумма индексов: ', index_sum)
