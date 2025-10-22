# Пространство имён класса

class Department:
    PYTHON_DEV = 0
    GO_DEV = 3
    REACT_DEV = 2


    # при создании метода в классе, ему не доступно пространство имён класса (PYTHON_DEV и т.д.)

    # этот код работать не будет
    # def info(self):
    #     print(PYTHON_DEV, GO_DEV, REACT_DEV)

        
    # Доступиться до имён можно следующими способами:
                          

    # через экземпляр класса
    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    # через класс
    def info2(self):
        print(Department.PYTHON_DEV, Department.GO_DEV, Department.REACT_DEV)

    # через свойство
    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    # через класс-метод
    @classmethod
    def info_cls(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    # через статик метод
    @staticmethod
    def info_static():
        print(Department.PYTHON_DEV, Department.GO_DEV, Department.REACT_DEV)   


# такая запись будет прибавлять сотрудника только в экземпляр класса
    def hiring_pyt_dev(self):
        self.PYTHON_DEV = self.PYTHON_DEV + 1

# такая запись будет прибавлять сотрудника в класс, не создавая записи в экземпляре класса
    def hiring_pyt_dev2(self):
        Department.PYTHON_DEV = Department.PYTHON_DEV + 1

it1 = Department()

it1.hiring_pyt_dev()
it1.hiring_pyt_dev()
print('it1 значение экземпляра = ', it1.PYTHON_DEV, 'значение класса = ', Department.PYTHON_DEV)
print('it1.__dict__ = ', it1.__dict__)

it2 = Department()

it2.hiring_pyt_dev2()
it2.hiring_pyt_dev2()
print('it2 значение экземпляра = ', it2.PYTHON_DEV, 'значение класса = ', Department.PYTHON_DEV)
print('it2.__dict__ = ', it2.__dict__)

# функции вообще сами в себе работают, никуда ничего не прибавляют...Только в самой функции видно действие
def main():
    it1.hiring_pyt_dev()
    it1.hiring_pyt_dev()

if __name__ == '__main__':
    main()