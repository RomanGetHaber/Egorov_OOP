# Магический метод __call__
# perf_counter подсчитывает время исполнения функции (финиш - стоп)
from time import perf_counter


# class Counter:
#     def __init__(self):
#         self.counter = 0
#         self.summa = 0
#         self.length = 0
#         print('init object', self)
#
# *args позволяет передавать переменное количество позиционных аргументов. Внутри функции такие аргументы собираются в кортеж.
# **kwargs позволяет передать переменное количество аргументов в виде пар "ключ - значение". Внутри функции такие аргументы собираются в словарь.
#     def __call__(self, *args, **kwargs):
#         self.counter += 1
#         self.summa += sum(args)
#         self.length += len(args)
#         print(f'наш экземпляр {self} вызывался {self.counter} раз')
#
#     def average(self):
#         return self.summa / self.length
#
#
# a1 = Counter()
# a1(1, 3, 5)
# a1(1, 8, 9, 1, 3)
# print(f'a1 summa = {a1.summa}, a1 len = {a1.length}, a1 counter = {a1.counter}')
# print(a1.average())

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Вызывается функция {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Функция отработала за {finish - start}')
        return result


@Timer
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# fact = Timer(fact)
print(fact(4))

fib = Timer(fib)
fib(4)
