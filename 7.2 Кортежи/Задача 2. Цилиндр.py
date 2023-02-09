import math
def cylinder(r, h):
    side = 2 * math.pi * r * h
    full = side + 2 * (math.pi * r ** 2)
    return side, full

r = int(input('Радиус: '))
h = int(input('Высота: '))

answer = cylinder(r, h)
print(answer)