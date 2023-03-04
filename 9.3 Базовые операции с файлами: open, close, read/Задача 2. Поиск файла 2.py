import os
import random

def find_file(search, file_name):
    all_path = []
    for i_elem in os.listdir(search):
        path = os.path.join(search, i_elem)
        if file_name == i_elem:
            all_path.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                all_path.extend(result)
    return all_path

# def check_file_inside(path_to_file):
#     file = open(path_to_file, 'r', encoding='utf8')
#     for line in file:
#         print(line)
#     file.close()

all_path = find_file('/Users/artemslavenko/Desktop', 'group_1.txt')
# check_file_inside(random.choice(all_path))

print(open(all_path[0]).read())