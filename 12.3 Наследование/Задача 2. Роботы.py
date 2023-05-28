class Robot:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return '\n Модель коробля {model}.'.format(
            model = self.__model,
        )

    def operat(self):
        print('\nРобот ездит по кругу!')

class WarRobot(Robot):
    def __init__(self, gun, model):
        super().__init__(model)
        self.gun = gun

    def operetion(self):
        print('\nРобот охраняет военные объект при помощи', self.gun)

class VacuumCleaningRobot(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.garbage_bad = 0

    def operation(self):
        print('\nРобот пылесосит пол.')

    def load(self):
        print('\nНачинаю уборку.')
        self.garbage_bad += 1
        print('\nТекущая загруженность ', self.garbage_bad)

    def unload(self):
        print('\nОчищаем контейнер.')
        if self.garbage_bad > 5:
            self.garbage_bad = 0
        else:
            print('\nУборка!')
            self.garbage_bad += 1
        print('\nТекущая загруженность ', self.garbage_bad)

class SubmarineRobot(WarRobot):
    def __init__(self, gun, model, depth):
        super().__init__(gun, model)
        self.depth = depth

    def operation(self):
        print('\nКорабль ведет боевое дежурство на глубине', self.depth)


robot = WarRobot('Пулимет', 'A5')
robot.operetion()