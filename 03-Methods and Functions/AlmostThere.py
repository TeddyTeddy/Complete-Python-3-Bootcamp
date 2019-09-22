# TASK
# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number


def almost_there(num):
    if abs(num-100) <= 10 or abs(num-200) <= 10:
        return True
    return False


print(f'almost_there(90): {almost_there(90)}')
print(f'almost_there(104): {almost_there(104)}')
print(f'almost_there(150): {almost_there(150)}')
print(f'almost_there(209): {almost_there(209)}')
