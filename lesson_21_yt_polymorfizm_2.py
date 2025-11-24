from lesson_21_yt_polymorfizm import Rectangle, Square, Circle

rect1 = Rectangle(2, 3)
rect2 = Rectangle(3, 5)
# print(rect1.get_rect_area, rect2.get_rect_area)

sq1 = Square(4)
sq2 = Square(5)
# print(sq1.get_square_area, sq2.get_square_area)

cir1 = Circle(4)
cir2 = Circle(5)
# print(cir1.get_circle_area, cir2.get_circle_area)

"""
Проблема - для каждой фигуры используется свой метод расчёта площади.
При использования такого метода приходится использовать множество if. 

figures = [rect1, rect2, sq1, sq2, cir1, cir2]
for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.get_rect_area)
        
    elif isinstance(figure, Square):
        print(figure.get_square_area)

    else:
        isinstance(figure, Circle)
        print(figure.get_circle_area)
        
Решение - полиморфизм
"""
figures = [rect1, rect2, sq1, sq2, cir1, cir2]
for figure in figures:
    print(figure, figure.get_area)