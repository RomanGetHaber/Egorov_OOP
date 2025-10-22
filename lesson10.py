# Геттеры и сеттеры, property атрибуты

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('бывший баланс ', self.__balance)
        # валидация вводимых данных кортежем, если не int и не float выводим ошибку
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом!')
        self.__balance = value
        print('новый баланс ', self.__balance)
    def delete_balance(self):
        print('удаляем баланс')
        del self.__balance

    # установка property атрибутов
    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

Ivan = BankAccount('Ivan', 100)

d = BankAccount('Misha', 300)

# использование property fset=set_balance
d.balance = 777
# использование property fget=get_balance
print(d.balance)

w = BankAccount('Piter', 8000)

# использование property fdel=delete_balance
del w.balance
print(w.__dict__)