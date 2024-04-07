class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, value):
        self._age = value

    @name.setter
    def name(self, word):
        self._name = word

    def __repr__(self):
        return "{}: {}".format(self._name, self._age)


first = Person('Artem', 35)
second = Person('Misha', 3)
third = Person('Masha', 6)
humans = [first, second, third]
print(humans)
humans.sort(key=lambda x: x.age)
print(humans)
humans.sort(key=lambda x: -x.age)
print(humans)
