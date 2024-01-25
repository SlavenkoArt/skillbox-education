# def smalles_divisor(N):
#     divider = 2
#     if N <= 1:
#         print('Ошибка ввода. Число должно быть больше 1')
#     while N % divider > 0:
#         divider += 1
#     return divider
#
# number = int(input('Введите число: '))
#
# divider = smalles_divisor(number)
# print('Наименьший делитель отличный от единицы: ', divider)

def smalles_divisor(N):
    divider = 2
    if N <= 1:
        print('Число должно быть больше 1')

    while N % divider > 0:
        divider += 1
    return divider

number = int(input('Введите число: '))

action = smalles_divisor(number)
print(f'Наименьший делитель отличный от единицы: {action}'.format(action))