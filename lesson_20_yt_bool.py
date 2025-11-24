# магические методы
# метод __bool__

'''
Числа - число будет правдивым, если оно отличается от нуля.
Строки - если строка состоит хотя бы из одного символа, то она будет 'True'
Колекции -  пустой список будет False, не пустой True

print(bool('kf'))  - True
print(bool(''))    - False
print(bool(123))   - True
print(bool(-78))   - True
print(bool(0))     - False
print([1])         - True
print([])          - False
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """
    Если не установлены методы __len__ и __bool__ то bool(Point) с любыми значениями будет выдавать True
    Первым делом смотреть программа будет смотреть в метод __len__ !!!
    
    
    Инициализируем метод __len__
    так как метод __len__  не поддерживает отрицательные числа, используем метод __abs__(преобразование в положительное)
    
    """

    def __len__(self):
        print('call __len__')
        return abs(self.x - self.y)

    """
    При использовании метода __len__, Point(5, 5) будет выдавать False т.к. 5-5=0, поэтому нужно использовать метод __bool__
    
    используем такое выражение:
    return self.x != 0 or self.y != 0
    если две координаты равны нулю вернётся False, если хоть одна координата не равна 0, то выражение будет True
    """
    def __bool__(self):
        print('call __bool__')
        return self.x != 0 or self.y != 0


p1 = Point(0, 0)
p2 = Point(1, 5)

print(bool(p1))

"""
Не явное использование метода bool, если р2 = True print('Hello')
"""
if p2:
    print('hello')
