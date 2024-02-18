
from abc import ABC, abstractmethod


class Transport(ABC):

    def __init__(self, color, speed):
        self._color = color
        self._speed = speed

    def move(self):
        pass

    def signal(self):
        pass

    @abstractmethod
    def ride_on_erth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value


class Car(Transport):
    def ride_on_erth(self):
        print('Едем в соседнее село.')


class Boat(Transport):
    def ride_on_water(self):
        print('Ходим по воде')


class MusicMixin:
    def play_music(self):
        print('Ла ла ла ла ла ла')


class Amhpibian(Car, Boat, MusicMixin):
    pass


amph_transport = Amhpibian('blue', 123)
amph_transport.ride_on_erth()
amph_transport.ride_on_water()
amph_transport.play_music()
print(amph_transport.color)
amph_transport.color = 'white'
print(amph_transport.color)
