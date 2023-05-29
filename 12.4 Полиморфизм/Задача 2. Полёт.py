class Can_Fly:
    def __init__(self):
        self.__height = 0
        self.__speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def to_land(self):
        self.height = 0
        self.speed = 0
        print('\nПолет закончен.')

    def info(self):
        return '{} высота {}, скорость {}'.format(
            self.__class__.__name__, self.height, self.speed
        )

class Butterfly(Can_Fly):
    def take_off(self):
        self.height = 1

    def fly(self):
        self.speed = 0,5

class Rocket(Can_Fly):
    def take_off(self):
        self.height = 500
        self.speed = 1000

    def to_land(self):
        self.height = 0
        self.speed = 0
        self.destroy_enemy_base()

    def destroy_enemy_base(self):
        print('Цель поражена!')


rocket = Rocket()
rocket.take_off()
print(rocket.info())
rocket.to_land()
print(rocket.info())