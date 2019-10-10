x = 50


def func():
    global x  # x is not added to local symbol table of func()
    print('This function is now using the global x!')
    print(locals()) # {}
    print('Because of global statement, x is: ',  globals()['x'])
    x = 2
    print('Ran func(), changed global x to', globals()['x'])


print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
