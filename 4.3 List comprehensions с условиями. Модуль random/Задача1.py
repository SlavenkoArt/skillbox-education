import random

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

summ = [i for i in range(first, second) if i % 2 == 0]

print(summ)