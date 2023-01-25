number = input('Введите число: ')
list_number = dict()

for num in range(1, int(number) + 1):
    list_number[num] = int(num) ** 2

print(list_number)