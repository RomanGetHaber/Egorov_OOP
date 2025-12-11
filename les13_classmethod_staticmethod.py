#Classmethod и staticmethod
class Example:
    def hello():
        print('этот метод вызывается только у класса')

    def instance_hello(self):
        print('этот метод вызовется только у экземпляра класса')

    @staticmethod
    def static_hello():
        print('этот метод вызовется и у класса и у экземпляра класса')

    @classmethod
    def class_hello(cls):
        print(f'работа с классами, {cls}')

Example.hello()
d = Example()
d.instance_hello()
Example.static_hello()
d.static_hello()

d.class_hello()