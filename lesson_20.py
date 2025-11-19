# ООП 19 Магические методы __eq__ и __hash__. Dunder methods в Python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and \
                self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(30, 40)

print(p1 == p2)
print(p1 == p3)

print(f' hash(p1) = {hash(p1)} hash(p2) = {hash(p2)}')
print(f' hash(p3) = {hash(p3)} ')