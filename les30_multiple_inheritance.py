# Множественное наследование

class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ура, я отучился на доктора')

    def can_cure(self):
        print('Я доктор, я могу лечить')

    def can_build(self):
        print('Я доктор, я тоже умею строить, но хуёво')


class Builder:

    def __init__(self, rank):
        self.rank = rank

    def can_build(self):
        print('Я строитель, я могу строить')

    def graduate(self):
        print('Ура, я отучился на строителя')

class Person(Doctor, Builder):

    def __init__(self, degree, rank):
        super().__init__(degree)
        Builder.__init__(self, rank)

    def __str__(self):
        return f'Person rank {self.rank}, degree {self.degree} '
    # def can_build(self):
    #     print('Я человек, я тоже могу строить')

p = Person(8, 9)
# p.can_build()
# метод __mro__ показывает порядок наследования (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>)
print(Person.__mro__)
p.graduate()

s = Person('spec', 6)
print(s)
