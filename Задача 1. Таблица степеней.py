numbers = [3,7,5]

while True:

 number = int(input('Новое число: '))

 numbers.append(number)

 print('Текущий список чисел:', numbers)

 for _ in numbers:

   print(_ ** 2, _ ** 3, _ ** 4)

 print()