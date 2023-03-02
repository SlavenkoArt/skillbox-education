import os

path_file = input('Введите путь: ')

if os.path.isdir(path_file):
    print('\n Это папка!')
elif os.path.isfile(path_file):
    print('Это файл!')
    print('Размер файла: ', os.path.getsize(path_file), 'байт')
else:
    print('Указанного пути не существует!')