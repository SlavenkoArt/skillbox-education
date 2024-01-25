class Unit:

    def __init__(self, hp):
        self.__hp = hp

    def set_hp(self, amount):
        self.__hp = amount

    def get_hp(self):
        return self.__hp

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - 0)  # -0 написан для наглядности, в теории  мы могли бы этого и не писать


class Soldier(Unit):

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount)


class Citizen(Unit):
    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount * 2)

soldier = Soldier(200)
citizen = Citizen(100)
while soldier.get_hp() > 0:
    soldier.get_damage(1)
    print(soldier.get_hp())

citizen.get_damage(50)

print(citizen.get_hp())
