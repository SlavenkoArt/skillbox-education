class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return '\nМодель корабля {model}'.format(
            model = self.__model
        )

    def sail(self):
        print('\n Корабль куда то поплыл!')


class Warship(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun
    def attack(self):
        print(f'\nКорабль аттакует из {self.gun}')


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print('\n Загружаем корабль')
        self.tonnage_load += 1
        print('\nТекущая загруженность ', self.tonnage_load)

    def unload(self):
        print('\nРазгружаем корабль!')
        if self.tonnage_load >0:
            self.tonnage_load -= 1
        else:
            print('\nКорабль уже разгружен.')
        print('\nТекущая загруженность ', self.tonnage_load)

warship = Warship('Волгодонск', 'Кинжал')
cargoship = CargoShip('Лев Толстой')
warship.attack()
cargoship.load()
