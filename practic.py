
class User:
    login_passwords = {}

    def __init__(self, login, password):
        self.__dict__ = User.login_passwords
        self.__login = login
        self.password = password


    @property
    def password(self):
        print('get password')
        return self.__password

    @password.setter
    def password(self, value):
        if not self.is_simple_password(value):
            raise ValueError('The simple_password.txt contains this password')
        self.__password = value

    @staticmethod
    def is_simple_password(password):
        with open('simple_password.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip() == password:
                    return False
            return True



a = User('ivan', 1010)
b = User('kozel', 4545)
print(User.login_passwords)
