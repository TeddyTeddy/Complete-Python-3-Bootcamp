try:
    x = 5
    y = 0

    z = x / y
except ZeroDivisionError:
    print('zero division occurred')
finally:
    print('All done!')
