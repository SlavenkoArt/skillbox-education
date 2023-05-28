class Coordinates():
    __count = 0
    __x = 0
    __y = 0
    points = int(input('Сколько будет координат?: '))
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'{self.__x, self.__y}'

    def check_value(self, value):
        if isinstance(value, str) and value.isdigit():
            value = float(value)
        if isinstance(value, (int, float)):
            return value
    def get_corX(self):
        return self.__x

    def get_corY(self):
        return self.__y

    def set_x(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__x = checker_value

    def set_y(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__y = checker_value
    def info(self):
        print('x = {}\ny = {}\ncount = {}'.format(self.__x, self.__y, self.__count))

    def point_count(self):
        for _ in range(self.points):
            cor_point = Coordinates(x=int(input('X: ')), y=int(input('Y: ')))
            Coordinates.__count += 1
            cor_point.info()

points = Coordinates()
print(f'x = {points.get_corX()}')
print(f'y = {points.get_corY()}')
points.point_count()
# points.info()