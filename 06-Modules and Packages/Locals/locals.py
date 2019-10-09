print(globals())   # {..., '__name__': '__main__', '__builtins__': <module 'builtins' (built-in)>}
def outer_function():
    print(locals())  # a should not be in local symbol table at this point; {}
    a = 20           # local symbol table is being modified with the addition of a referring to 2
    print(locals())  # a is added to the local symbol table at this point; {'a': 20}

    class A:
        pass

    def inner_function():
        print(locals())  # a should not be in local symbol table at this point; {}
        a = 30
        print(locals())  # a is added to the local symbol table at this point; {'a': 30}
        print('a =', a)

    print(locals())
    #   {'a': 20, 'A': <class '__main__.outer_function.<locals>.A'>,
    # '   inner_function': <function outer_function.<locals>.inner_function at 0x7f3ce1799ea0>}
    inner_function()
    print('a =', a)

print(globals())
# {..., '__name__': '__main__', '__builtins__': <module 'builtins' (built-in)>,
#  'outer_function': <function outer_function at 0x7f5e2cde1ea0>}
a = 10
print(globals())
# {..., '__name__': '__main__', '__builtins__': <module 'builtins' (built-in)>,
#  'outer_function': <function outer_function at 0x7f5e2cde1ea0>, 'a': 10}
outer_function()
print('a =', a)