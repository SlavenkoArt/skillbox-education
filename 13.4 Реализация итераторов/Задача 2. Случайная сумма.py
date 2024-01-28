import random

class RandomSumm:
    def __init__(self, limit):
        self.__limit = limit
        self.__countr = 0
        self.__number = 0


    def __iter__(self):
        return self

    def __next__(self):
        self.__countr += 1
        if self.__countr > self.__limit:
            raise StopIteration
        self.__number += random.random()
        return self.__number


counter = RandomSumm(5)
for i in counter:
    print(i)