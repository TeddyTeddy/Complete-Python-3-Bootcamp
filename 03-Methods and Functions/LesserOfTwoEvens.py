# TASK:
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd


def is_even(x):
    return x % 2 == 0


def lesser_of_two_evens(a,b):
    if is_even(a) and is_even(b):
        if b > a:
            return a
        else:
            return b
    else: # if one or both numbers are odd
        if b > a:
            return b
        else:
            return a


print(f'lesser_of_two_evens(2,4): {lesser_of_two_evens(2,4)}')
print(f'lesser_of_two_evens(2,5): {lesser_of_two_evens(2,5)}')


