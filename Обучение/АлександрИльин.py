flat_number = 20

entrance_number = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1
print('Номер квартиры: ', entrance_number)
print('Этаж: ', floor_number)
