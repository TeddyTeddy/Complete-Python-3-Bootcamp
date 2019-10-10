# global x
x = 50


def func(x):  # x as an argument creates a local variable! Shadows name 'x' from outer scope
    print(locals())
    print('x in func is', x)
    x = 2
    print('In func, changed local x to', x)
    print(locals())


func(x)
print('In global scope, x is still', globals()['x'])