def ask_user(qwestion,
             complaint = 'Неверный ввод. Пожалуйста введите да или нет.',
             retries = 4):
    while True:
        answer = input(qwestion).lower()
        if answer == 'да':
            return 1
        if answer == 'нет':
            return 0
        retries -= 1
        if retries == 0:
            print('Количество попыток истекло.')
            break
        print(complaint)
        print('Осталось попыток: ', retries)

ask_user('Вы действительно хотите выйти? ')
ask_user('Удалить файл? ')
ask_user('Записать файл? ')