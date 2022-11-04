word_list = []
counts = [0, 0, 0]

for i in range(3):
    print('Введите ', i + 1, 'слово: ', end='')
    word = input()
    word_list.append(word)

text = input('Введите слово из текста: ')
while text != 'end':
    for index in range(3):
        if word_list[index] == text:
            counts[index] += 1
    text = input('Введите слово из текста: ')

print('\nПодсчет слов в текст')

for i in range(3):
    print(word_list[i], ': ', counts[i])