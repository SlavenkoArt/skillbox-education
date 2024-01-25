# print("Введите первую точку")
# x1 = float(input('X: '))
# y1 = float(input('Y: '))
# print("\nВведите вторую точку")
# x2 = float(input('X: '))
# y2 = float(input('Y: '))
#
# x_diff = x1 - x2
# y_diff = y1 - y2
# if x1 - x2 == 0:
#     x_diff = x1
# if y1 - y2 == 0:
#     y_diff = y1
# k = y_diff / x_diff
# b = y2 - k * x2
#
# print("Уравнение прямой, проходящей через эти точки:")
# print("y = ", k, " * x + ", b)

print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
if x_diff == 0:
    x_diff = x1
y_diff = y1 - y2
if y_diff == 0:
    y_diff = y1
k = y_diff / x_diff
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)