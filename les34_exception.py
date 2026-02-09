# Exception
def third():
    print('start third')
    1/0
    print('finish third')

def second():
    print('start second')
    third()
    print('finish second')

def first():
    print('start first')

    print('finish first')

print('hello')
first()
# print('hello')
# print('hello')
# print('hello')
# try:
#     a = [1, 2][5]
#     print(a)
# except IndexError:
#     print('неправильный индекс')
#
# print('hello')
# 1/0
# print('hello')