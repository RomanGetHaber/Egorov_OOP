# Магические методы
# метод __getitem__, __setitem__, __delitem__

class Vector:
    def __init__(self, *args):
        # сохраняем в self.values список с переменным количеством аргументов
        self.values = list(args)

    def __repr__(self):
        # str(self.values) будет выводить список аргументов, вместо ячейки памяти объекта
        return str(self.values)

    # Проблема написанного кода выше в том что мы не можем обратиться к экземпляру класса по индексу (проблема!)
    # v1 = Vector(1, 2, 5)
    # print(v1[1])

     # __getitem__ отвечает за доступ к элементам экземпляра класса по индексу или ключу
    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за границами нашей коллекции')

    # v2 = Vector(3, 8, 5432)
    # print(v2[2])

    # пробуем заменить значение по индексу (проблема!)
    # v2[1] = 100
    # TypeError: 'Vector' object does not support item assignment
    # наш класс не поддерживает изменение значения по индексу
    # print(v2)

    # __setitem__ это метод, который позволяет изменять значения в объекте по индексу или ключу
    # def __setitem__(self, key, value):
    #     if 0 <= key < len(self.values):
    #         self.values[key] = value
    #     else:
    #         raise IndexError('Индекс за границами нашей коллекции')

# v3 = Vector(3, 12, 9)
# v3[2] = 'dfksk'
# print(v3)

# если мы попытаемся удалить значение по индексу (проблема!)
# v4 = Vector(3, 12, 9)
# del v4[0]
# AttributeError: __delitem__

    # __delitem__ позволяет удалить значение объекта по ключу
    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами нашей коллекции')

# v5 = Vector(3, 12, 23, 'kfjkd', 23, 45)
# print(v5)
# del v5[3]
# print(v5)

# Хитрости этих методов!

#     def __getitem__(self, item):
#         # изменяем порядок индексов, чтобы начинался с индекса 1 и заканчивался последним по счёту
#         if 1 <= item <= len(self.values):
#             return self.values[item-1]
#         else:
#              raise IndexError('Индекс за границами нашей коллекции')
# v6 = Vector(3, 13, 18)
# print(v6[3])

    # с __setitem__ можем создать разряженный список, где индексы не вошедшие в диапазон заполняются нулями [2, 4, 5, 5, 0, 0, 0, 0, 0, 25]
    def __setitem__(self, key, value):
        if 1 <= key <= len(self.values):
            self.values[key-1] = value
        elif key>len(self.values):
            diff = key - len(self.values)
            self.values.extend([0]*diff)
            self.values[key-1] = value
        else:
            raise IndexError('Индекс за границами нашей коллекции')
v7 = Vector(2, 4, 5, 5)
v7[10] = 25
print(v7)
