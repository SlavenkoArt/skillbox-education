words = [input('Введите слово ') for _ in range(3)]
text = input('Введите текст ').split()
words_count = [text.count(word) for word in words]

print(words_count)