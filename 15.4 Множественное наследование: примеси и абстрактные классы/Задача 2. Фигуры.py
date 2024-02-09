from abc import ABC, abstractmethod

class Figure(ABC):
    """
    абстрактный базовый класс Фигура

    Args and attrs:
        pos_x (int) координата х
        pos_y (int) координата у
        length (int) длина фигуры
        width (int) ширина фигуры
    """

    def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizebleMixin:
    def resize(self, length: int, width: int) -> None:
        self.length = length
        self.width = width


class Rectangle(Figure, ResizebleMixin):
    """ Квадрат. Родительский класс: Figure. """
    pass


class Square(Figure, ResizebleMixin):
    """ Прямоугольник. Родительский класс: Figure. """
    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        super().__init__(pos_x, pos_y, size, size)
    pass


rect1 = Rectangle(pos_x=5, pos_y=5, length=10, width=15)
rect2 = Rectangle(pos_x=7, pos_y=3, length=5, width=11)
squq = Square(pos_x=10, pos_y=20, size=10)


for figure in [rect1, rect2, squq]:
    new_size_x = figure.length * 2
    new_size_y = figure.width * 2
    figure.resize(new_size_x, new_size_y)


Figure.move(1, 1, 1)