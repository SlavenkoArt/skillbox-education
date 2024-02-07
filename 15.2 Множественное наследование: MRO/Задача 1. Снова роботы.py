

class Robot:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def __str__(self):
        res = super.__str__()
        return res + '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Я - робот')



class CanFly():
    def __init__(self, *args, **kwargs):
        self.altitude = 0 #метров
        self.velocity = 0 #км/ч

    def takeoff(self):  #Взлететь
        self.altitude = 100
        self.velocity = 300

    def flight(self): #Полет
        self.altitude = 5000

    def will_land(self): #Приземлится
        print('Захожу на посадку')
        self.altitude = 0
        self.velocity = 0

    def operate(self):
        super().operate()
        print('Летим')

    def __str__(self):
        res = super().__str__()
        return res + ' {} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity,
        )


class ScoutDrone(CanFly, Robot):
    def __init__(self, model):
        super().__init__(model=model)

    def operate(self):
        super().operate()
        print('\nВедем разведку с воздуха')

class WarRobot(CanFly, Robot):
    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print('\nРобот охраняет военные объект при помощи', self.gun)


print()
ScoutDrone('a1').operate()
print()
WarRobot('Z1000', 'палки').operate()
