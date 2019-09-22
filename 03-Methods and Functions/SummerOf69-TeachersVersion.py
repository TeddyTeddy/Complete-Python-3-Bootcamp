# TASK
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections
# of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(int_lst):
    total = 0
    add = True
    for num in int_lst:
        if add:
            if num == 6:
                add = False
            else:
                total += num
        if not add:
            if num == 9:
                add = True
    return total


print(f'summer_69([]): {summer_69([])}')
print(f'summer_69([1, 3, 5]): {summer_69([1, 3, 5])}')
print(f'summer_69([4, 5, 6, 7, 8, 9]): {summer_69([4, 5, 6, 7, 8, 9])}')
print(f'summer_69([2, 1, 6, 9, 11]): {summer_69([2, 1, 6, 9, 11])}')


def summer_69_v2(int_lst):
    total = 0
    add = True
    for num in int_lst:
        while add:  # is add operation allowed by the previous num in the previous for iteration?
            if num == 6:
                add = False
            else:  # if num is 6, turn off add flag for the next for iteration
                total += num
                break
        while not add:
            if num == 9:  # if num is 9, turn on add flag for the next for iteration
                add = True
            else:  # if num is not 9, do nothing for num and break the while not add
                break
    return total


print(f'summer_69_v2([]): {summer_69_v2([])}')
print(f'summer_69_v2([1, 3, 5]): {summer_69_v2([1, 3, 5])}')
print(f'summer_69_v2([4, 5, 6, 7, 8, 9]): {summer_69_v2([4, 5, 6, 7, 8, 9])}')
print(f'summer_69_v2([2, 1, 6, 9, 11]): {summer_69_v2([2, 1, 6, 9, 11])}')
print(f'summer_69_v2([1, 2, 3, 6, 7, 9, 5, 6, 3, 9, 9, 4]): {summer_69_v2([1, 2, 3, 6, 7, 9, 5, 6, 3, 9, 9, 4])}')

