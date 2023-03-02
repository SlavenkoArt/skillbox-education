import os

def find_file(search, file_name):
    for i_elem in os.listdir(search):
        path = os.path.join(search, i_elem)
        if file_name == i_elem:
            print(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result


search = input('Ищем в: ')
file_name = input('Имя файла: ')

find_file(search, file_name)