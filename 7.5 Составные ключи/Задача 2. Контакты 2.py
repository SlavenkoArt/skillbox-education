phonebook = {}
print('\nВведите в графе Фамиля end для завершения.\n')

while True:
    surname = input('Фамилия: ')
    if surname == 'end':
        break
    name = input('Имя: ')
    phoneNumber = input('Номер телефона: ')
    if (surname, name) in phonebook:
        print('Такой пользователь существует.')
    else:
        phonebook[(surname, name)] = phoneNumber
        for i_key, i_meaning in phonebook.items():
            print(f'{i_key} - {i_meaning}')


