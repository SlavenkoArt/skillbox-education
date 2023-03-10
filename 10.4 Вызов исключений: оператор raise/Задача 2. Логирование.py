def palindrom(word):
    return word == word[::-1]

words_count = 0
line_count = 0


with open('words.txt', 'r', encoding='utf8') as text, open('errors.log', 'w', encoding='utf8') as log_file:
    try:
        for sym in text:
            line = sym.rstrip('\n')
            if line.isalpha():
                words_count += palindrom(line)
            else:
                raise ValueError("строка не полностью состоит из букв!")
        print(words_count)
        log_file.close()

    except ValueError as exc:
        log_file.write(str(exc))

