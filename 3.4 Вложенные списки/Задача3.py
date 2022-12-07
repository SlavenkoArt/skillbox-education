goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

new_price = [input('Новый фрукт: '), int(input('Цена: '))]

goods.append(new_price)

for i in goods:
    i[1] += (i[1] / 100) * 8

print(goods)
