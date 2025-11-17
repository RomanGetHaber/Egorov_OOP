# ООП 15 Магические методы. Методы __str__ и __repr__. (Dunder methods)
from queue import PriorityQueue


class Lion:
    def __init__(self, name):
        self.name = name

    # добавляет информацию для разработчиков, если __str__ не присвоен то в консоле также отображается эта же информация
    def __repr__(self):
        return f'The object Lion - {self.name}'

    # добавляет информацию для отображения в консоле (для пользователя)
    def __str__(self):
        return f'Lion - {self.name}'

a = Lion('Anton')
print(repr(a))

b = Lion('Simba')
print(b)

class Otrezok:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

# т.к. метод len не принимает отрицательные значения используем abs - такая запись вызовет магический метод __abc__
    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(self.x2 - self.x1)

f = Otrezok(55, 5)
print(len(f))
print(Otrezok.__dict__)
print(Lion.__dict__)

