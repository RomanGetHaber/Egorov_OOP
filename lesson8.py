# Моно-состояние для экземпляров класса

class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }
    def __init__(self):
        self.__dict__ = Cat.__shared_attr



a = Cat()
b = Cat()


a.name = 'Djosef'                    # добавляем новый атрибут "name"в экземпляр класса Cat,
                                     # который присваивается всем экземплярам класса
                                     # т.к. в атрибуте класса Cat используется словарь __shared_atr

b.breed = 'siam'                     # при изменении атрибута экземпляра класса происходит тоже-самое
print(
    f''' a.__dict__ = {a.__dict__},'
 b.__dict__ = {b.__dict__}'''
)