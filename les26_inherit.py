# Наследование Введение

class Person:
    def can_walk(self):
        print('Могу ходить')

    def can_breathe(self):
        print('Могу дышать')


class Doctor(Person):
    def can_cure(self):
        print('Я могу лечить')

class Ortoped(Doctor):
    pass


class Architect(Person):
    def can_build(self):
        print('Я могу построить здание')

d = Doctor()
a = Architect()
o = Ortoped()
print(d.can_cure())
print(a.can_build())
print(issubclass(Doctor, Person)) # спрашиваем является Doctor ли подклассом Person - ответ True
