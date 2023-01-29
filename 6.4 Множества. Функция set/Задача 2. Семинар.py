import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

nums_1 = set(nums_1)
nums_2 = set(nums_2)

print('\n1-е множество: ', nums_1)
print('2-е множество: ', nums_2)

print('\nМинимальное число 1-го множества: ', nums_1.pop())
print('Минимальное число 2-го множества: ', nums_2.pop())

print('\nМинимальное число 1-го множества: ', nums_1)
print('Минимальное число 2-го множества: ', nums_2.pop())

print('\nПервое без элемента', nums_1)
print('Второе без элемента ', nums_2)

first_random = random.randint(100, 200)
seconde_random = random.randint(100, 200)
print('\nСлучайное число для 1-го множества: ', first_random)
print('Случайное число для 2-го множества: ', seconde_random)

nums_1.add(first_random)
nums_2.add(seconde_random)

print('\nОбъединение множеств: ', nums_1.union(nums_2))

print('\nПересечение множеств: ', nums_1.intersection(nums_2))

print('\nЭлементы входящие в nums_2, но не входящие в nums_1: ', nums_2.difference(nums_1))