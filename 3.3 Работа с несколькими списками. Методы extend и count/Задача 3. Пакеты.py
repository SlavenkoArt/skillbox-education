pack_sum = int(input('Количество пакетов?: '))

packages_sum = []
error = 0

for i in range(pack_sum):
    print('Пакет номер', i + 1)
    countr = 0
    packages = []
    for num in range(4):
        print(num + 1, 'бит: ')
        bit = int(input(''))
        if bit < 0:
            countr += 1
            packages.append(bit)
        else:
            packages.append(bit)
    if countr > 1:
        print('Много ошибок в пакете.')
        error += 1
    elif countr <= 1:
        packages_sum.extend(packages)
    print('\n')

print('Полученное сообщение: ', packages_sum, 'Количество ошибок в сообщении: ', error, 'Количество потерянных'
                                                                                        ' пакетов ', error)