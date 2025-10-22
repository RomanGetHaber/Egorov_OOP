class Square:
    def __init__(self, s):
        self.__side = s
        self.__perimetr = None

    @property
    def perimetr(self):
        if self.__perimetr is None:
            print('высчитываю периметр квадрата')
            self.__perimetr = self.__side * 4
        return self.__perimetr

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__perimetr = None

d = Square(5)
print(d.perimetr)
d.side = 12
print(d.perimetr)
print(d.perimetr)
