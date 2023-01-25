
phone_number = dict()

while True:
    print("\nТекущие контакты на телефоне:\n")
    if phone_number:
        for name in phone_number:
            print(name, phone_number[name])
    else:
        print("<Пусто>")
    new_name = input("\nВведите имя (для остановки введите end): ")
    if new_name == 'end':
        break
    elif new_name in phone_number:
        print("\nОшибка: такое имя уже существует.")
    else:
        new_phone = int(input("Введите номер телефона: "))
        phone_number[new_name] = new_phone