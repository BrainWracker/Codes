class Figure:
    perimeter = 1
    area = 1
    color = 'b'
    def __init__(self, perimeter, area, color):
        if not(isinstance(perimeter, int)) or not(isinstance(area, int)) or perimeter <= 0 or area <= 0 or color not in ['r', 'g', 'b']:
            raise ValueError('Invalid value')
        self.perimeter = perimeter
        self.area = area
        self.color = color

class Polygon(Figure):
    angle_count = 3
    equilateral = True
    biggest_angle = 45
    def __init__(self, perimeter, area, color, angle_count, equitaletiral, biggest_angle):
        super().__init__(perimeter, area, color)
        if not(isinstance(angle_count, int)) or angle_count < 3 or not(isinstance(equitaletiral, bool)) or not(isinstance(biggest_angle, int)) or biggest_angle <= 0:
            raise ValueError('Invalid value')
        self.angle_count = angle_count
        self.equilateral = equitaletiral
        self.biggest_angle = biggest_angle

    def __str__(self):
        return f'Polygon: Периметр {self.perimeter}, площадь {self.area}, цвет фигуры {self.color}, количество углов {self.angle_count}, равносторонний {self.equilateral}, самый большой угол {self.biggest_angle}.'

    def __add__(self):
        return self.perimeter + self.area

    def __eq__(self, other):
        if self.perimeter == other.perimeter and self.area == other.area and self.angle_count == other.angle_count:
            return True
        else:
            return False


class Circle(Figure):
    radius = 3
    diametr = 2*radius
    def __init__(self, perimeter, area, color, radius, diametr):
        super().__init__(perimeter, area, color)
        if not (isinstance(radius, int)) or radius <= 0 or not isinstance(diametr, int) or diametr <= 0 or diametr != 2*radius:
            raise ValueError('Invalid value')
        self.radius = radius
        self.diametr = diametr

    def __str__(self):
        return f'Circle: Периметр {self.perimeter}, площадь {self.area}, цвет фигуры {self.color}, радиус {self.radius}, диаметр {self.diametr}.'

    def __add__(self):
        return self.perimeter + self.area

    def __eq__(self, other):
        return True if self.radius == other.radius else False

class PolygonList(list):
    name = 'name'
    def __init__(self, name):
        super().__init__()
        self.name = name
    def append(self, p_object):
        if isinstance(p_object, Polygon):
            super().append(p_object)
        else:
            raise TypeError(f'Invalid type {type(p_object)}')
    def print_colors(self):
        i = 1
        for poly in self:
            print(f'{i} многоугольник: {poly.color}')
            i += 1
    def print_count(self):
        print(len(self))

class CircleList(list):
    name = 'name'
    def __init__(self, name):
        super().__init__()
        self.name = name

    def extend(self, iterable):
        iterable = filter(lambda i: isinstance(i, Circle), iterable)
        super().extend(iterable)

    def print_colors(self):
        i = 1
        for cir in self:
            print(f'{i} окружность: {cir.color}')
            i += 1

    def total_area(self):
        return sum(map(lambda c: c.area, self))
