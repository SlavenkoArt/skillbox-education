try:
    new_file = open('new_file.txt', 'w', encoding='utf8')
    text = input('Введите текст: ')
    new_file.write('Текст сообщения: \n')
    new_file.write(text)
except (FileNotFoundError, PermissionError) as exc:
    print(type(exc), exc)
except ValueError as exc:
    print(type(exc), exc)
except Exception as exc:
    print(type(exc), exc)
else:
    print('Запись прошла без ошибок.')
finally:
    if new_file and not new_file.close():
        new_file.close()