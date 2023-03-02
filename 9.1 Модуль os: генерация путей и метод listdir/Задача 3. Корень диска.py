import os

print('Корень диска: ', os.path.abspath('.').split('\\')[0])
print('Корень диска 2: ', os.getcwd())