# Публичные, приватные, защищенные атрибуты и методы (public, protected, private)
class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):                             # метод который читает приватную функцию
        print(self.__print_private_data())

    def print_protected_data(self):                         # защищённые атрибуты допустим (self._name) не понял для чего
        print(self._name, self._balance, self._passport)

    def __print_private_data(self):                          # сделали приватным сам метод
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('Bob', 10000, 45466565)

print(account1.__dict__)
# print(account1.__name)
# print(account1._balance)
# print(account1.passport)

account1.print_public_data()

print(dir(account1))                                  # смотрим все атрибуты и методы, включая приватные
print(account1.__dict__)                              # смотрим установленные атрибуты и методы, включая приватные

print(account1._BankAccount__passport)                # распечатываем приватный атрибут экземпляра класса

print(account1._BankAccount__print_private_data())   # распечатываем приватный метод экземпляра класса

                                                    # чтобы защитить по настоящему данные от доступа нужно использовать
                                                    # модуль который называется accessify
