class Car():
    # свойства
    car_count = 0 # Это статическое свойство
    # методы
    def start(self, name, make, model): # Это динамическое свойство
        print('The engine is started')
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1
# Создадим объект класса Car, и вызовем метод start
car_a = Car()
car_a.start('Corolla', 'Toyota', 2015) # The engine is started
print(car_a.name) # Corolla
print(car_a.car_count) # 1
# Создадим ещё один объект(экземпляр), и вызовем метод start
car_b = Car()
car_b.start('City', 'Honda', 2008) # The engine is started
print(car_b.name) # City
print(car_b.car_count) # 2
# Теперь мы перепишем метод start таким образом что бы превратить статическое свойство класса в динамическое свойство объекта
class Car():
    # свойства
    car_count = 0
    # методы
    def start(self, name, make, model):
        print('The engine is started')
        self.name = name
        self.make = make
        self.model = model
        self.car_count += 1 # всего навсего мы обратились к статическому свойству класса через параметр self, и вот он уже
        # динамическое
car_a = Car()
car_a.start('Corolla', 'Toyota', 2015) # The engine is started
print(car_a.name) # Corolla
print(car_a.car_count) # 1

car_b = Car()
car_b.start('City', 'Honda', 2008) # The engine is started
print(car_b.name) # City
print(car_b.car_count) # 1
# мы получили еденичку, это связано с тем, что это свойство, теперь свойство объекта!!!!! И оно теперь пренадлежить
# свойству класса!!!