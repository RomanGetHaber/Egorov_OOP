# Декоратор Property (Property decorator)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('бывший баланс ', self.__balance)
        if not isinstance(value, (int, float)):              # валидация вводимых данных кортежем, если не int и не float
            raise ValueError('Баланс должен быть числом!')   # выводим ошибку
        self.__balance = value
        print('новый баланс ', self.__balance)
    def delete_balance(self):
        print('удаляем баланс')
        del self.__balance

    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)


Ivan = BankAccount('Ivan', 100)

d = BankAccount('Misha', 300)

d.balance = 777                # использование property fset=set_balance
print(d.balance)               # использование property fget=get_balance

w = BankAccount('Piter', 8000)

del w.balance                  # использование property fdel=delete_balance
print(w.__dict__)

x = property()
