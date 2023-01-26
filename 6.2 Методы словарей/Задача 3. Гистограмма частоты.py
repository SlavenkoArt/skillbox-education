def histogram(text):
    text_dict = dict()
    for sym in text:
        if sym in text_dict:
            text_dict[sym] += 1
        else:
            text_dict[sym] = 1
    return text_dict

text = input('Введите текст: ').lower()
hist = histogram(text)

for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

print('Максимальное значение: ', max(hist.values()))