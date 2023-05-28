class People:
    __count = 0

    def __init__(self, age, name):
        self.__age = age
        self.__name = name
        People.__count += 1

    def __str__(self):
        return f'Возраст: {self.__age} Имя: {self.__name}'

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_count(self):
        return self.__count

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст.')

artem = People(34, 'Артем')
misha = People(2, 'Миша')
print(misha.get_count())
new_age = 80
misha.set_age(new_age)
print(misha.get_age())
