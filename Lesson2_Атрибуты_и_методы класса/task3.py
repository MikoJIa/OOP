""""Определите класс 'Прямая' со свойствами: координаты двух
точек (x1, y1), (x2, y2), и методами:  вывод уравнения прямой и
определение точек пересечения с осями координат"""

class Direct():
    x1 = 4.3
    y1 = -1.2
    x2 = -8.5
    y2 = 4

    def print_eqution_direct(self):
        k = (self.y2 - self.y1) / (self.x2 - self.x1)
        b = self.y1 - k * self.x1
        print(f'Уравнение прямой: y = {round(k, 2)} * x + {round(b, 2)}')


    def point_intersection(self, x = 0, y = 0):
        self.x = x
        self.y = y





d = Direct()
d.print_eqution_direct()


