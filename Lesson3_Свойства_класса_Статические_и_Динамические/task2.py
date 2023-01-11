# """
# Измените класс “Вектор” следующим образом:
# - добавьте статическое свойство - точка отсчета (x1, y1, z1), -
# имеющее одинаковое значение для всех объектов класса;
# - три существующие свойства - декартовы координаты (x, y, z) -
# “превратите” в одно динамическое свойство - конец вектора (x2, y2, z2), -
# устанавливаемое в новом методе определения вектора;
# - внесите соответствующие изменения в методы класса.
#
# -------------
# Тестовые значения:
# (4, 12, 6) -> 14
# (3, 7, 2) -> 7.87
# """

from math import sqrt

class Vector():
    start_point = (1, 1, 5)


    def end_vector(self, x, y, z):
        self.end_point = (x, y, z)
        # вычисляем координаты вектора, исходя из координат точек начала и конца
        self.x = x - Vector.start_point[0]
        self.y = y - Vector.start_point[1]
        self.z = z - Vector.start_point[2]

    def print(self):
        print(f'vector: ({self.x}; {self.y}; {self.z})')

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

v1 = Vector()
v1.end_vector(4, 12, 6)
v1.print()
print(f'modul: {v1.len_vector()}')
v1.mult_vector(5)
v1.mult_vector(3)
print('--------------')
v2 = Vector()
v2.end_vector(3, 7, 2)
v2.print()
print(f'modul: {v2.len_vector()}')
v2.mult_vector(5)
v2.mult_vector(3)