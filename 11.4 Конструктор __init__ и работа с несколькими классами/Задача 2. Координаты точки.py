class Coordinates():
    count = 0
    points = int(input('Сколько будет координат?: '))
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def info(self):
        print('x = {}\ny = {}\ncount = {}'.format(self.x, self.y, self.count))

    def point_count(self):
        for _ in range(self.points):
            cor_point = Coordinates(x=int(input('X: ')), y=int(input('Y: ')))
            Coordinates.count += 1
            cor_point.info()

points = Coordinates()
points.point_count()
# points.info()
