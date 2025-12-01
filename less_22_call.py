# Магический метод __call__

class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter +=1
        self.summa += sum(args)
        self.length += len(args)
        print(f'наш экземпляр {self} вызывался {self.counter} раз')


a1 = Counter()
a1(1, 3, 5)
a1(1, 8, 9, 1)
print(f'a1 summa = {a1.summa}, a1 len = {a1.length}, a1 counter = {a1.counter}')