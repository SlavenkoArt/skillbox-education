# N = input("Введите число:" )
# amount = 0
# summ = 0
#
# for symbol in N:
#     amount += 1
#
# N = int(N)
#
# while N != 0:
#     summ += N % 10
#     N = N // 10
#
# print('Сумма чисел: ', summ)
# print('Количество цифр в чисел: ', amount)
# print('Разность суммы и количества цифр: ', abs(summ - amount))

N = input('Введите число: ')

summ = 0

amount = len(N)

N = int(N)

while N != 0:
    summ += N % 10
    N = N // 10

print('Сумма чисел: {}\n'
      'Количество цифр в числе: {}\n'
      'Разность суммы и количества цифр:{}'.format(summ,
                                                      amount, abs(summ - amount)))