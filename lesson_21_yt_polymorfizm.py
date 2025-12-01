# Полиморфизм
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} * {self.b} = '

    @property
    # def get_rect_area(self):
    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'{self.a} * {self.a} = '

    @property
    # def get_square_area(self):
    def get_area(self):
        return self.a**2

class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'{self.r} * 3,14 = '

    @property
    # def get_circle_area(self):
    def get_area(self):
        return 3.14 * self.r**2

r1 = Rectangle(2, 5)
r2 = Rectangle(4, 12)
sq1 = Square(4)
cir1 = Circle(12)

def main():
    print(r1, r1.get_area)
    print(r2, r2.get_area)
    print(sq1, sq1.get_area)
    print(cir1, cir1.get_area)



if __name__ == '__main__':
    main()