"""
3)Создать класс точки, реализовать конструктор который
инициализирует 3 координаты (Class): Определенный программистом тип данных.x, y, z).
Реалзиовать методы для получения и изменения каждой из координат.

Перегрузить для этого класса методы сложения, вычитания, деления и умножения.
Перегрузить один любой унарный метод.
Ожидаемый результат: умножаю точку с координатами 1,2,3 на
другую точку с такими же координатами, получаю результат 1, 4, 9.
"""


class Coord:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        pass

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, value):
        self.x = value

    def set_y(self, value):
        self.y = value

    def set_z(self, value):
        self.z = value

    # вариант 2 set/get

    def set_dot(self, dot, value):
        if dot == 'x':
            self.x = value
        elif dot == 'y':
            self.y = value
        elif dot == 'z':
            self.z = value

    def get_dot(self, dot):
        if dot == 'x':
            return self.x
        elif dot == 'y':
            return self.y
        elif dot == 'z':
            return self.z

    # сложение
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return x, y, z

    # вычитание
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return x, y, z

    # деление
    def __truediv__(self, other):
        try:
            x = self.x / other.x
            y = self.y / other.y
            z = self.z / other.z
            return x, y, z
        except ZeroDivisionError:
            return f'Division by zero is forbidden'

    # умножение
    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return x, y, z
        pass

    # унарный
    def __neg__(self):
        return Coord(-self.x, -self.y, -self.z)


coord_1 = Coord(1, 2, 3)
coord_2 = Coord(1, 2, 3)

print(coord_1 - coord_2)
print(coord_1 + coord_2)
print(coord_1 * coord_2)

coord_2.set_dot('z', 0)
print(f'Z:{coord_2.get_dot("z")}')
print(coord_1 / coord_2)
