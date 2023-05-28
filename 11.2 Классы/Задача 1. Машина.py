import random

class Toyota:
    color = 'Красный'
    price = '1.000.000'
    max_speed = 200
    current_speed = 0

toyota1 = Toyota()
toyota2 = Toyota()
toyota3 = Toyota()

toyota1.max_speed = random.randint(0, 201)
toyota2.max_speed = random.randint(0, 201)
toyota3.max_speed = random.randint(0, 201)

print(toyota1.max_speed)
print(toyota2.max_speed)
print(toyota3.max_speed)