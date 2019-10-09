x = 5


def func():
    print(x)


class A:
    pass


print(globals())  # 'x': 5, 'func': <function func at 0x7f3fa08ebe18>, 'A': <class '__main__.A'>
