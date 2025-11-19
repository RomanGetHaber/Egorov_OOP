# ООП 18 Специальные методы сравнения объектов классов

# Магические методы сравнения
# __eq__ - отвечает за == equals (равно)
# __ne__ - отвечает за != not equals (не равно)
# __lt__ - отвечает за < less than (меньше)
# __le__ - отвечает за <= less than or equals (меньше или равно)
# __gt__ - отвечает за > greater than (больше)
# __ge__ - отвечает за >= greater than or equals (больше или равно)

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('__eq__ call')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print('__lt__ call')
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __gt__(self, other):
        print('__gt__ call')
        if isinstance(other, Rectangle):
            return self.area > other.area
        elif isinstance(other, (int, float)):
            return self.area > other

    def __le__(self, other):
        return self==other or self<other

v = Rectangle(2, 4)
u = Rectangle(3, 4)
print(u <= 25)
print(u.area)