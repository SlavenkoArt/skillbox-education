left = int(input('Левая граница: '))
right = int(input('Правая граница: '))

cube = [i ** 3 for i in range(left, right + 1)]
square = [i ** 2 for i in range(left, right + 1)]

print('Список кубов чисел от ', left, 'до ', right, ': ', cube)
print('Список квадратов чисел от ', left, 'до ', right, ': ', square)
