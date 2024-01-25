# def count(first_year, second_year):
#     for symbol in range(first_year, second_year + 1):
#         first_veriable = symbol // 1000
#         second_veriable = (symbol // 100) % 10
#         third_veriable = (symbol // 10) % 10
#         fourth_veriable = symbol % 10
#         if (second_year == third_veriable == fourth_veriable) or \
#             (first_veriable == second_veriable == third_veriable) or \
#             (first_veriable == third_veriable == fourth_veriable) or \
#             (first_veriable == second_veriable == fourth_veriable):
#             print(symbol)
#         return symbol
#
# first_year = int(input('Введите первый год: '))
# second_year = int(input('Введите второй год: '))
#
# print('Годы от ', first_year, 'до ', second_year, 'с тремя одинаковыми цифрами:')
# three_numbers = count(first_year, second_year)
# print(three_numbers)


def count_year(first_year, second_year):
    for number in range(first_year, second_year + 1):
        first_number = number // 1000
        second_number = (number // 100) % 10
        third_number = (number // 10) % 10
        fourth_number = number % 10
        if (first_number == second_number == third_number) or\
            (second_number == third_number == fourth_number) or\
            (third_number == fourth_number == first_number) or\
            (fourth_number == first_number == second_number):
            print(number)


def count_len(year):
    if len(year) > 4 or len(year) < 4:
        print('Введите четырехзначное число: ')
        return False
    else:
        return True


first_number = int(input('Введите первый год: '))
second_number = int(input('Введите второй год: '))

while count_len(str(first_number)) == False:
    first_number = int(input('Введите первый год: '))

while count_len(str(second_number)) == False:
    second_number = int(input('Введите второй год: '))

print('Год от {} до {} с тремя одинаковыми цифрами: '.format(first_number, second_number))
cou = count_year(first_number, second_number)
print(cou)