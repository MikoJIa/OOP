# метод - это некоторая функция, находящаяся внутри класса и выполняющая определённую работу, связанную с объектом
# данного класса
# Классификация Методов бывает:
# Статические.
# Уровня класса. - обязательно создание объекта
# Классовые.

# Методы уровня класса это наши обычные методы которые мы уже научились определятьв предыдущих уроках
class Car():
    car_count = 0  # Это статическое свойство
    # Вот он метод уровня класса
    def start(self, name, make, model):  # Это динамическое свойство
        print('The engine is started')
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

# Декоратор(дискриптор) - это некоторая функция, которая позволяет преобразовывать функуции и методы их определения.
# Для того что бы объявить метод статическим или классовым необходимо использовать так называемый ДЕКОРАТОРЫ(ДИСКРИПТОРЫ)
@staticmethod
def my_method():
    return 'some method'
# Эта запись эквивалентна вот это записи:
def my_method():
    return 'some method'

my_method = staticmethod(my_method)

# Классовые методы занимают некое промежуточное место между статическими методами и обычными.
# классовые методы первым пораметром принимают класс
# классовые методы(@classmethod) - методы, изменяющие состояние самого класса.
# классовые методы могут менять состояние самого класса и это изменение отразится сразу на всех объктах класса.

class Car():
    car_count = 0  # Это статическое свойство

    @classmethod
    def inc_car_count(cls):
        cls.car_count += 1 # теперь мы можем обращатся к статическому свойству класса

    def start(self, name, make, model):  # Это динамическое свойство
        print('The engine is started')
        self.name = name
        self.make = make
        self.model = model
        Car.inc_car_count()
# далее создаём экземпляр данного класса
c = Car()
print(Car.car_count) # 0
c.start('Corolla', 'Toyota', 2015) # The engine is started
print(Car.car_count) # 1
Car.inc_car_count()
print(Car.car_count) # 2
c.inc_car_count()
print(c.car_count) # 3
c1 = Car() # создаём ещё один объкт
print(c1.car_count) # 3

# Статический метод
# Статические методы(@staticmethod) - это метод, которые "не знают", к какому классу они относятся.
# статические методы прикреплины к классу только для удобства и не могут менять ни состояние класса, ни состояние объкта.
class D():
    @staticmethod
    def test(x):
            return x == 0
# далее обращаемся к этому статическому методу через класс
print(D.test(1)) # False
# создаём экземпляр данного класса
d = D()
print(d.test(0)) # True
# Давайт передадим этот статический метод нашему классу Car

class Car():
    car_count = 0  # Это статическое свойство

    @classmethod
    def inc_car_count(cls):
        cls.car_count += 1 # теперь мы можем обращатся к статическому свойству класса

    @staticmethod
    def is_valid_model(model):
        models = ('Toyota', 'Honda', 'Hyandai', 'Nissan', 'Audi', 'Mazda')
        return model in models

    def start(self, name, make, model):  # Это динамическое свойство
        print('The engine is started')
        self.name = name
        self.make = make
        self.model = model
        Car.inc_car_count()

print(Car.is_valid_model('Honda')) # True
print(Car.is_valid_model('Example')) # False
c = Car()
print(c.is_valid_model('Toyota')) # True

# Как и когда использовать тип метода

# методы уровня класса - пренадлежат объктам и получают доступ к ним через параметр self

# классовые мемтоды - принадлежат классу и получают доступ к нему чере параметр cls

# статические методы - принадлежат классу, но нен имеют доступа ни к самому классу, ни к его объктам
