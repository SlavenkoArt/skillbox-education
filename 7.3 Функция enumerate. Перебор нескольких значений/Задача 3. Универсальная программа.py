text = 'О Дивный Новый мир!'
new_text = []
text_list = [100, 200, 300, 'буква', 0, 2, 'а']
new_text_list = []

for index, sym in enumerate(text):
    if index % 2 == 0:
        new_text.append(sym)
print(new_text)

for index, sym in enumerate(text_list):
    if index % 2 == 0:
        new_text_list.append(sym)
print(new_text_list)