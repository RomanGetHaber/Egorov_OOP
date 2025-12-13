# Slots, property и наследование

class Rectangle:
    __slots__ = 'length', 'weight'

    def __init__(self, length, weight):
        self.length = length
        self. weight = weight

    @property
    def perimetr(self):
        return (self.length + self.weight)*2

    @property
    def area(self):
        return self.length * self.weight

a = Rectangle(4, 5)
print(a.area, a.perimetr)

# Не доделал урок, лень матушка...