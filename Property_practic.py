from string import digits

class User:
     def __init__(self, login, password):
         self.login = login
         self.password = password

     def __str__(self):
         return f'объект класса {self.__class__}'

     @staticmethod
     def is_include_digit(password):
         for digit in digits:
             if digit in password:
                 return True
         return False

     @property
     def password(self):
         return self.__password

     @password.setter
     def password(self, value):
         if not isinstance(value, str):
             raise TypeError('Пароль должен быть строкой')
         elif len(value) < 8:
             raise ValueError('Пароль слишком короткий, длина пароля должна быть более 8-ми символов')
         elif len(value) > 12:
             raise ValueError('Пароль слишком длинный, длина пароля должна быть менее 12-ти символов')
         elif not User.is_include_digit(value):
             raise ValueError('Пароль должен содержать хотя бы одну цифру')
         else:
            self.__password = value

user = User('jon', '12sdfsdf34')
user.password = "jhhjklhlkjl1"
print(user.password)
print(User.is_include_digit('kdgfksgk11'))
b = User('ivan', 14445555523)
print(b.login, b.password)


