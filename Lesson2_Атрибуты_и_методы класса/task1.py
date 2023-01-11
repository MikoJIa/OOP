"""
Определить класс “Дробь” со свойствами: числитель и знаменатель, -
и методами: вывод дроби на экран, определение обратной дроби и сокращение дроби.
"""
class Fraction():
    numerator = 12
    denomenator = 30
    # Необходимо выводить дробъ на экран
    # Что бы сделать настоящюю дробъ в питоне необходимо прописать особый символ UNICODE.ORG записываем та '\u'- обозна-
    # ет нижнее подчёркивание для текста символ имеет код '\u0332'
    def print(self):
        print('\u0332'.join(f'  {self.numerator} '))
        print(f'  {self.denomenator}')
    # Следующий метод определение обратной дроби
    def get_reversed(self):
        # выведим на экран сообщение что этот метод делает
        print('The reversed fraction of')
        # теперь вызываем метод собственный
        self.print()
        # печатаем продолжение фразы
        print('is: ')
        # создаём новый объект типа дробъ
        rev_fr = Fraction()
        # просто меняем местами значения
        rev_fr.numerator = self.denomenator
        rev_fr.denomenator = self.numerator
        # теперь осталось только распечатать полученую дробъ
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
            self.numerator //= a
            self.denomenator //= a
            # теперь распечатаем ту дробъ которую получили после сокращения
            self.print()
        else:
# если наша дробъ не может быть сокращена
            print('The fraction')
            self.print()
            print("can't be reduction")


    # Сразу создадим объект(экземпляр), что бы смотреть как он работает
f1 = Fraction()
f1.print()
f1.get_reversed()
f1.fr_redaction()