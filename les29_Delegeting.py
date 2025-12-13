# Наследование Делегирование Delegating

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Person {self.name} {self.surname}'

    def info(self):
        print('Parent class')
        print(self)

    def breathe(self):
        print('Человек дышит')


class Doctor(Person):

    def __init__(self, name, surname, age):
        # В первую очередь нужно ставить родительский класс "super()", что бы не перезаписать данные если вдруг в родительском
        # классе появится переменная self.age = age
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name} {self.surname}'

    def breathe(self):
        print('Доктор дышит')


p = Person('Inan', 'Petechkin')
d = Doctor("Petr", 'Petrov', 45)
print(p.__dict__)
print(d.__dict__)

d.info()
p.info()