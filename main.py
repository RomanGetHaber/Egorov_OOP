
class Cat:

    def __init__(self, name, breed='pers', age=1, color='blue'):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        print('hello new object is ', self, name, breed, color, age)


bob = Cat('Bob')
tom = Cat('Tom', 'siam', 12, 'black')

