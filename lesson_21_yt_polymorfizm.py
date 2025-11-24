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

def main():
    r1 = Rectangle(2, 5)
    print(r1)

if __name__ == '__main__':
    main()