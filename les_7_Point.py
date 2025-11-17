from math import sqrt

class Point:

    list_points = []

    def __init__(self, coord_x=1, coord_y=1):
        self.moove_to(coord_x, coord_y)
        self.list_points.append(self)

    def moove_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.moove_to(0, 0)

    def print_point(self):
        print(f'координаты точки: x={self.x} y={self.y}')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Точка')
        else:
            return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)

p1 = Point()
p1.moove_to(5, 6)
p1.moove_to(2, 2)
p1.name = 'p1'
p2 = Point(8, 12)
print(Point.list_points)

for i in Point.list_points:
    print(f'x = {i.x}, y = {i.y}')
# p1=Point()
# p2=Point()
# p2.moove_to(5, 4)
# p1.moove_to(-4, 1)
# print(p1.calc_distance(p2))
# print(p1.print_point())
#
# print(-9**2)
#
# p7=Point(6, 0)
# p8=Point(0, 8)
#
# print(p7.calc_distance(p2))
#
# p9=Point()
# p10=Point()
# for i in Point.list_points:
#     print(f'x = {i.x}   y = {i.y}')
#
# print(Point.list_points[0].x)
#
# p15=Point()
# p16=Point()
#
# print(p15.print_point())
#
# print(sqrt(25))
