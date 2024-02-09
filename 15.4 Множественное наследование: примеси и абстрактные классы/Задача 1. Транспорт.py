from abc import ABC, abstractmethod


class Transport(ABC):

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


amph_transport = Amhpibian()
amph_transport.ride_on_erth()
amph_transport.play_music()
amph_transport.signal()
amph_transport.move()
amph_transport.ride_on_water()
