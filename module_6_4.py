import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = []
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

        self._color = None
        self.filled = True
        self.set_color(color[0], color[1], color[2])


    def get_color(self):
        return self._color

    def __is_valid_color(self, r, g, b):
        for val in [r, g, b]:
            if not (isinstance(val, int) and 0 <= val <= 255):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color = (r, g, b)
        # else:
        #     print(f'Нельзя установить цвет: ({r}, {g}, {b})')

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        # else:
        #     print(f'Нельзя установить стороны: {new_sides}')

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count or not self.__is_valid_triangle(*sides):
            sides = (1, 1, 1)
        super().__init__(color, *sides)

    def __is_valid_triangle(self, a, b, c):
            result = a + b > c and b + c > a and c + a > b
            return result

    def get_square(self):
        s = len(self) / 2
        a, b, c = self.get_sides()
        result = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return result

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        sides = [side] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())