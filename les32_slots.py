# Slots
"""
По умолчанию Python хранит атрибуты каждого объекта в словаре __dict__, что позволяет гибко добавлять новые атрибуты, но занимает дополнительную память и имеет накладные расходы на поиск.

Когда мы объявляем в классе __slots__ — мы ограничиваем список допустимых атрибутов и заменяем словарь на более компактное внутреннее представление, что:

уменьшает память на каждый объект;
ускоряет доступ к атрибутам (нет обращения к словарю), но;
лишает возможность добавлять новые атрибуты, не описанные в __slots__.

"""
from timeit import timeit
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    # ограничение атрибутов. В этом случае пропадает метод __dict__
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_c11():
    s = Point(3, 4)
    s.x = 100
    del s.x

def make_c12():
    s = PointSlots(3, 4)
    s.x = 100
    del s.x

# проверка времени исполнения функций
print(timeit(make_c11))
print(timeit(make_c12))

# проверка, сколько занимает места объект
p = Point(4, 6)
q = PointSlots(4, 6)

print(p.__sizeof__())
print(q.__sizeof__())







# Якобы Применение __slots__ действительно призвано уменьшать расход памяти на объекты и потенциально повышать производительность
# ... Но мои вычисления показывают наоборот)

# Тест предложенный chatGPT 4.1 mini
def test_memory_and_speed():
    import sys

    N = 10**7

    # Создание списка объектов без слотов
    points = [Point(i, i) for i in range(N)]

    # Создание списка объектов с слотами
    points_slots = [PointSlots(i, i) for i in range(N)]

    print("Размер объекта Point:", sys.getsizeof(points[0]))
    print("Размер объекта PointSlots:", sys.getsizeof(points_slots[0]))

    # Замер времени создания
    import time

    start = time.time()
    for i in range(N):
        p = Point(i, i)
    print("Время создания Point:", time.time() - start)

    start = time.time()
    for i in range(N):
        p = PointSlots(i, i)
    print("Время создания PointSlots:", time.time() - start)

test_memory_and_speed()