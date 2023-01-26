small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

print('Товар на складе: \n')
for storage in big_storage:
    print(storage, big_storage[storage])

while True:
    product = input('\nВведите название товара (для выхода введите пробел): \n').lower()
    if product == ' ':
        break
    elif product in big_storage:
        print(product, ' - ', big_storage[product])
    elif not product in big_storage:
        print(product, 'нет в списке товаров')
