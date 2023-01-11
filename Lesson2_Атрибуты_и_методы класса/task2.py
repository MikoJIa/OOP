# """
# Определить класс “Вектор” со свойствами: 3 декартовы координаты (x, y, z), -
# и методами: вывод вектора на экран, вычисление длины вектора и умножение вектора на число.
#
# -------------
# Тестовые значения:
# (4, 12, 6) -> 14
# (3, 7, 2) -> 7.87
# """
from math import sqrt

class Vector():
    x = 4
    y = 12
    z = 6

    def print(self):
        print(f'{self.x}; {self.y}; {self.z}')

    def len_vector(self):
        # Формула вычисления длины вектора len(v) = v(x^2 + y^2 + z^2)
        # Импортируем одну функцию(модуль)
        length = sqrt(self.x**2 + self.y**2 + self.z**2)
        return round(length, 2)
    # Умножение вектора на число
    # Тут мы уже будем принимать параметр, число на которое будем умножать наш вектор
    def mult_vector(self, num):
        self.x *= num
        self.y *= num
        self.z *= num
        print('New vector: ')
        self.print()

v = Vector()
v.print()
print(f'modul: {v.len_vector()}')
v.mult_vector(3)
v.mult_vector(5)