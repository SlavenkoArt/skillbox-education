text = input('Введите текст: ')

kit = set(".,;:!?")
kit_countr = 0

# print('Количество знаков пунктуации: ', len(text.intersection(kit)))

for sym in text:
    if sym in kit:
        kit_countr += 1

print('Количество знаков пунктуации: ', kit_countr)
