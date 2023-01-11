# Изменить классы 'Дробъ' и 'Вектор' следующим образом:
# 1. Все статические свойства классов должны изменятся только внутри классовых методов
# 2. Выделить один или несколько вспомогательных методов(если это не было сделано ранее) и оформить их в виде статических
# методов

class Fraction():
    correct_fr_count = 0
    incorrect_fr_count = 0
# должны изменятся только в нитри классовых методов
# Сразу добавим это классовый метод
    @classmethod
    def inc_fr_count(cls, is_proper):
        if is_proper:
            cls.correct_fr_count += 1
        else:
            cls.incorrect_fr_count += 1


# свойства класса - числитель и знаменатель - должны быть динамическими и
    # # определяться внутри нового метода
    def set(self, numerator, denomenator):
        self.denomenator = denomenator
        self.numerator = numerator
# здесь мы вызываем наш классовый метод
        Fraction.inc_fr_count(numerator < denomenator)


    def print(self):
        print('\u0332'.join(f'  {self.numerator} '))
        print(f'  {self.denomenator}')

    def get_reversed(self):
        print('The reversed fraction of')
        self.print()
        print('is: ')
        rev_fr = Fraction()
        rev_fr.set(self.denomenator, self.numerator)
        rev_fr.print()
# определим этот метод как статический
    @staticmethod
    def get_nod(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def fr_redaction(self):

        nod = Fraction.get_nod(self.numerator, self.denomenator)

        if nod != 1:
            print('The fraction')
            self.print()
            print('after reduction of')
                # теперь мы сокращаем нашу дробъ
            self.set(self.numerator // nod, self.denomenator // nod)
                # теперь распечатаем ту дробъ которую получили после сокращения
            self.print()
        else:
                # если наша дробъ не может быть сокращена
            print('The fraction')
            self.print()
            print("can't be reduction")

f1 = Fraction()
f1.set(5, 10)
f1.print()
f1.get_reversed()
f1.fr_redaction()
f2 = Fraction()
f2.set(8, 3)
f2.print()
f3 = Fraction()
f3.set(11, 11)
f3.print()
# f1.get_reversed()
f3.fr_redaction()
f4 = Fraction()
f4.set(12, 36)
f4.print()
f4.fr_redaction()
f5 = Fraction()
f5.set(3, 2)
f5.print()
print(f'Proper fraction count: - {Fraction.correct_fr_count}')
print(f'Improper fraction count: - {Fraction.incorrect_fr_count}')