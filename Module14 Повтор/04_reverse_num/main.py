# def first_part(N):
#     number = 0
#     main_part = round(N,1) // 1
#     while main_part > 0:
#         rest=main_part % 10
#         main_part = main_part // 10
#         number = number * 10
#         number = number + rest
#     return number
#
# def second_part(N):
#     number2 = 0
#     whole = round((N % 1) * 100, 2)
#     main_part = round(whole, 1) // 1
#     while main_part > 0:
#         rest = main_part % 10
#         main_part = main_part // 10
#         number2 = number2 * 10
#         number2 = number2 + rest
#         number2 = number2
#     number2 = number2 / 100
#     return number2
#
# N1 = float(input('Введите первое число: '))
#
# first_part_backwards = first_part(N1)
# second_part_backwards = second_part(N1)
# backwardsF = first_part_backwards + second_part_backwards
#
# N2 = float(input('Введите второе число: '))
#
# first_part_backwards = first_part(N2)
# second_part_backwards = second_part(N2)
# backwardsS = first_part_backwards + second_part_backwards
#
# summ = round(backwardsF + backwardsS, 1)
# print('Первое число наоборот: ', backwardsF)
# print('Первое число наоборот: ', backwardsS)
# print('Сумма: ', summ)

def first_part(N):
    number = 0
    main_path = round(N, 1) // 1
    while main_path > 0:
        rest = main_path % 10
        main_path = main_path // 10
        number = number * 10
        number = number + rest
    return number

def second_part(N):
    number = 0
    whole = round((N % 1) * 100, 2)
    main_path = round(whole, 1) // 1
    while main_path > 0:
        rest = main_path % 10
        main_path = main_path // 10
        number = number * 10
        number = number + rest
    number = number / 100
    return number

N1 = float(input('Введите первое число: '))

first_number_part1 = first_part(N1)
first_number_part2 = second_part(N1)
vice_first = first_number_part1 + first_number_part2

N2 = float(input('Введите второе число: '))

second_number_part1 = first_part(N2)
second_number_part2 = second_part(N2)
vice_second = second_number_part1 + second_number_part2

summ = vice_first + vice_second


print(f'Первое число: {vice_first}\nВторое число {vice_second}\nСумма: {summ}')
print(summ)