# Магические методы
# метод __iter__, __next__

class Mark:
    def __init__(self, values):
        self.value = values
        self.index =0

    def __iter__(self):
        return self

    def __next__(self):
        print('call __next__ marks')
        if self.index>=len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index +=1
        return letter


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

# мы не можем обойти объект циклом for (проблема!)

# igor = Student('Igor', 'Nikolaev', [2, 3, 5, 3, 2])
# for i in igor:
#     print(i) # TypeError: 'Student' object is not iterable

    # если в вашем классе реализован метод __getitem__, то питон воспользуется им для обхода вашей коллекции
    def __getitem__(self, item):
        print('call __getitem__')
        return self.surname[item]

# igor = Student('Igor', 'Nikolaev', [2, 3, 5, 3, 2])
# for i in igor:
#     print(i)

    # но главным способом обхода коллекции является метод __iter__, и при итеррации питон воспользуется именно им
    # def __iter__(self):
    #     print('call __iter__')
    #     return iter(self.surname)


# как работает "итерирование" списков(?)
# a = [1, '323', 2]
# b = iter(a)
# print(b) # <list_iterator object at 0x00000164573864A0>
# print(next(b)) # 1
# print(next(b)) # '323'
# c = a.__iter__()
# print(c)  # <list_iterator object at 0x00000164573864A0>
# print(c.__next__()) # 1
# print(c.__next__()) # '323'
# print(c.__next__()) # 2
# print(c.__next__()) # ошибка StopIteration

# igor = Student('Igor', 'Nikolaev', [2, 3, 5, 3, 2])
# for i in igor:
#     print(i)

# проблема всего вышесказанного в том что __iter__ применяет метод __next__ к классу str, а нам нужно применять к нашему классу Student
# делаем свою собственную полную итерацию. Создаём отдельный класс Mark над Students
    def __iter__(self):
        print('call __iter__')
        self.index = 0
        return iter(self.marks) # именно из за self.marks итерация проводится только по нему, а не по name и surname..

    def __next__(self):
        print('call __next__ students')
        if self.index>=len(self.surname):
            raise StopIteration
        letter = self.surname[self.index]
        self.index +=1
        return letter

m = Mark([2, 3, 5, 3, 2])
igor = Student('Igor', 'Nikolaev', m) # тут у нас m - это отдельный класс Mark, и используется его __next__
for i in igor:
    print(i)
