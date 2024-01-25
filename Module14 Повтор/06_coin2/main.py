# def segment_lenght (x, y):
#      import math
#      lenght = math.sqrt(x ** 2 + y ** 2)
#      return lenght
#
# print('Введите координаты монетки: ')
# x =float(input('X: '))
# y = float(input('Y: '))
# radius = float(input('Введите радиус: '))
#
# if radius >= segment_lenght(x,y):
#     print('Монетка где то рядом ')
# else:
#     print('Монетки в области нет')

def segment_lenght (x, y):
    import math
    lenght = max(x, y)
    return lenght

print('Введите координаты монетки: ')
x =float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))

if radius >= segment_lenght(x,y):
    print('Монетка где то рядом ')
else:
    print('Монетки в области нет')

