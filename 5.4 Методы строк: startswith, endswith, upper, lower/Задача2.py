way = input('Путь к файлу: ')

disk = input('На каком диске должен лежать: ')
extension = input('Требуемое расширение файла: ')

if way.startswith(disk) and way.endswith(extension):
    print('Путь корректен!')
else:
    print('Путь некорректен!')
