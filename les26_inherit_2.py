# Наследование Переопределение Overriding

class Person: # parent

    def __init__(self, name):
        # print('init Person')
        self.name = name

    def breathe(self):
        print('человек дышит')

    def walk(self):
        print('человек идёт')

    def sleep(self):
        print('человек спит')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()


    def __str__(self):
        class_name = str(self.__class__)
        return f'{class_name[len(class_name)-8:len(class_name)-2]} {self.name}'

class Doctor(Person):

    # Переопределяем метод, внутри дочернего класса создать такой же метод (с таким же названием) как у родительского класса
    # и определяем в нем другое поведение
    def breathe(self):
        print('доктор дышит')


class Architect(Person): # subclass (подкласс, дочерний класс)
    pass

a = Person('Petr')
d = Doctor('Ivan')


d.combo()
