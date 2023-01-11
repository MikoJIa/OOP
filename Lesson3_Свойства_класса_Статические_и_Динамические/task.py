# """
# Измените класс “Дробь” следующим образом:
# - свойства класса - числитель и знаменатель - должны быть динамическими и
# определяться внутри нового метода, задающего значение дроби;
# - добавьте 2 статических свойства - количество правильных и неправильных дробей, -
# которые должны отображать количество созданных объектов класса соответствующих типов.
#
# """

class Fraction():
    correct_fr_count = 0
    incorrect_fr_count = 0

# свойства класса - числитель и знаменатель - должны быть динамическими и
    # # определяться внутри нового метода
    def set(self, numerator, denomenator):
        self.denomenator = denomenator
        self.numerator = numerator

        if numerator >= denomenator:
            Fraction.incorrect_fr_count += 1
        else:
            Fraction.correct_fr_count += 1

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

    def fr_redaction(self):
            # давайте сохраним чеслитель и знаменатель в новых переменных
        a = self.numerator
        b = self.denomenator
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a

        if a != 1:
            print('The fraction')
            self.print()
            print('after reduction of')
                # теперь мы сокращаем нашу дробъ
            self.set(self.numerator // a, self.denomenator // a)
                # теперь распечатаем ту дробъ которую получили после сокращения
            self.print()
        else:
                # если наша дробъ не может быть сокращена
            print('The fraction')
            self.print()
            print("can't be reduction")

        # Сразу создадим объект(экземпляр), что бы смотреть как он работает

f1 = Fraction()
f1.set(5, 10)
f1.print()
f1.fr_redaction()
f2 = Fraction()
f2.set(8, 3)
f2.print()
f3 = Fraction()
f3.set(11, 11)
f3.print()
# f1.get_reversed()
f3.fr_redaction()
print(f'Proper fraction count: - {Fraction.correct_fr_count}')
print(f'Improper fraction count: - {Fraction.incorrect_fr_count}')
