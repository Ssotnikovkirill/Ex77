class Shape:
    def __init__(self, position, scale, color):
        self._position = None
        self._scale = None
        self._color = None

    def set_coord(self, position):
        if type(position) in (list, dict):
            self._position = position
        else:
            raise ValueError('Используй тип list или dict!')

    def get_coord(self):
        return self._position

    def set_scale(self, scale):
        self._scale = scale

    def get_scale(self):
        return self._scale

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def info(self):
        print('Position:', self.get_coord(), ' Scale:', self.get_scale(), ' Color:', self.get_color())

    def area(self):
        print('Площадь фигуры.')


class Rectangle(Shape):
    def __init__(self, position, scale, color, side1, side2):
        super().__init__(position, scale, color)
        self._side1 = side1
        self._side2 = side2

    def set_side1(self, side1):
        self._side1 = side1

    def get_side1(self):
        return self._side1

    def set_side2(self, side2):
        self._side2 = side2

    def get_side2(self):
        return self._side2

    def info(self):
        super().info()
        print('Side1: ', self.get_side1(), 'Side2: ', self.get_side2())

    def area(self):
        super().area()
        print('(прямоугольник) =', self.get_side1() * self.get_side1(), 'кв. ед.')


class Trapezoid(Shape):
    def __init__(self, position, scale, color, side1, side2, h):
        super().__init__(position, scale, color)
        self._side1 = side1
        self._side2 = side2
        self._h = h

    def set_side1(self, side1):
        self._side1 = side1

    def get_side1(self):
        return self._side1

    def set_side2(self, side2):
        self._side2 = side2

    def get_side2(self):
        return self._side2

    def set_h(self, h):
        self._h = h

    def get_h(self):
        return self._h

    def info(self):
        super().info()
        print('Side1: ', self.get_side1(), 'Side2: ', self.get_side2(), 'h: ', self.get_h())

    def area(self):
        super().area()
        print('(трапеция) =', 0.5 * (self.get_side1() + self.get_side1()) * self.get_h(), 'кв. ед.')


class Circle(Shape):
    def __init__(self, position, scale, color, radius):
        super().__init__(position, scale, color)
        self._radius = radius

    def set_radius(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def info(self):
        super().info()
        print('Radius: ', self.get_radius())

    def area(self):
        super().area()
        print('(окружность) =', 3.14 * self.get_radius() * self.get_radius(), 'кв. ед.')


C = Circle([3, 4], 56, 'red', 5)
T = Trapezoid([5, 7], 9, 'black', 4, 5, 11)
R = Rectangle([12, 29], 8, 'purple', 5, 4)

C.area()
T.area()
R.area()
