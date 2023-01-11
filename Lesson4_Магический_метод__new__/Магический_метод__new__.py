# Магический метод __new__ вызывается непосредственно перед созданием объкта класса!!!
# А вот другой магический метод __init__ вызывается  непосредственно после создания объкта класса!!!

class Point():
    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для ' + str(cls))
        return super().__new__(cls)

    def __init__(self, x = 0, y = 0):
        print('Вызов __init__ для ' + str(self))
        self.x = x
        self.y = y

pt = Point(1, 2)
print(pt)

# Паттерн Singleton

class DataBase():
    __instance = None # __instance - будет ссылкой на экземпляр класса
    # Для создания объектом на необходимо определить магический метод __new__
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединение БД')

    def read(self):
        return 'данные из БД'

    def write(self, data):
        print(f'запись в БД {data}')

# Создадим экземпляр класса
db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 90)
db.connect()
db2.connect()
