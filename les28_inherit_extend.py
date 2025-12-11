# Наследование Расширение Extending

class Person:
    age = 25

    def breathe(self):
        print('человек дышит')

    def slip(self):
        print('человек спит')

    def combo(self):
        self.breathe()
        self.slip()
        # если в родительском классе не будет нужного метода, программа выдаст ошибку AttributeError: 'Person' object has no attribute 'walk'
        if hasattr(self, 'walk'):
            self.walk()
        if hasattr(self, "age"):
            print(self.age)


class Doctor(Person):

    age = 30

    def sleep(self):
        print('доктор спит')

    def walk(self):
        print('доктор идёт')


p = Person()
d = Doctor()
p.combo()
print('-' * 10)
d.combo()