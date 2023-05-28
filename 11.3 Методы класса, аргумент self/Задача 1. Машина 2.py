import random

class Toyota:
    color = 'Красный'
    price = 1e6
    max_speed = 200
    current_speed = 0

    def info(self):
        print(self.color, self.price, self.max_speed, self.current_speed)

    def speed(self, new_speed):
        self.current_speed = new_speed

toyota1 = Toyota()
toyota2 = Toyota()
toyota3 = Toyota()

toyota1.max_speed = random.randint(0, 201)
toyota2.max_speed = random.randint(0, 201)
toyota3.max_speed = random.randint(0, 201)

print(toyota1.max_speed)
print(toyota2.max_speed)
print(toyota3.max_speed)

car = Toyota()
car.info()
car.speed(100)
print('-' * 10)
car.info()
print(Toyota.current_speed)