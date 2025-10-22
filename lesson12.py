class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    """
    Вычисляет площадь квадрата с ленивой инициализацией (Lazy Evaluation).
    
    При первом обращении вычисляет и кэширует значение площади.
    При последующих обращениях возвращает кэшированное значение,
    избегая повторных вычислений.
    """
    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.side**2
        return self.__area

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None


a = Square(5)
b = Square(10)

print(a.area)
print(a.area)
print(a.area)
print(b.area)
print(b.area)