ip_adress = "{0}.{1}.{2}.{3}"
count = 0
number = []

while count < 4:
    new_number = int(input('Введите число: '))
    if 0 <= new_number <= 255:
        number.append(new_number)
        count += 1

print(ip_adress.format(*number))