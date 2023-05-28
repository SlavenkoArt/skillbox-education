import random

class Toyota:
    color = 'Красный'
    price = 1e6
    max_speed = 200
    current_speed = 0

    def __init__(self, current_speed):
        self.current_speed = current_speed

    def info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}\n'.format(

        self.color, self.price, self.max_speed, self.current_speed))


toyota1 = Toyota(100)
toyota2 = Toyota(150)
toyota3 = Toyota(180)
toyota1.info()
toyota2.info()
toyota3.info()