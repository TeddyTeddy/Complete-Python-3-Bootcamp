# TASK
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False


def has_33(num_list):
    result = False
    for index, num in enumerate(num_list):
        if num == 3:  # check next: is the next number 3 also?
            if len(num_list) > (index + 1):  # is there a next number in num_list?
                if num_list[index+1] == 3:  # is the next number 3 also
                    result = True
                    break
    return result


print(f'has_33([1, 3, 3]): {has_33([1, 3, 3])}')
print(f'has_33([1, 3, 1, 3]): {has_33([1, 3, 1, 3])}')
print(f'has_33([3, 1, 3]): {has_33([3, 1, 3])}')
print(f'has_33([3]): {has_33([3])}')
