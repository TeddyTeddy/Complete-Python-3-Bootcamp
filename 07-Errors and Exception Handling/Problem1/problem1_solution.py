for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except TypeError:
        print('TypeError occurred when executing i**2')
