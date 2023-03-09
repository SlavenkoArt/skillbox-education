file_ages = None
file_result = None

try:
    file_ages = open("ages.txt", "r", encoding="utf8")
    file_result = open("result.txt", "x", encoding="utf8")
    # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
except (FileExistsError, PermissionError) as exc:  # названия исключений можно группировать в кортежи
    print("Поймано исключение: ", exc, type(exc))

if file_result and file_ages:
    names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    count = 0
    for line in file_ages:
        try:
            file_result.write(names[count] + " - " + str(line))
            count += 1
        except (ValueError, TypeError) as exc:
            print("Поймано исключение: ", exc, type(exc))