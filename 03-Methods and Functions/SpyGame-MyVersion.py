# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


def is_end_of_list(lst, index):
    return len(lst) <= index

#  int_list = [1,0,4,0,0,7,7]
def pick(pick_me_list, int_list):
    """
    Returns a filtered list containing only the numbers in the pick_me_list
    :param pick_me_list: a tuple of numbers to look for in int_list (i.e. (0,7)
    :param int_list: a list containing only integers (i.e. [1,0,4,0,0,7,7] )
    :return: a filtered version of int_list containing only the numbers in pick_me_list.
    Note that the numbers in the output list are in the order of presence in int_list
    (i.e. [0,0,0,7,7] )
    """
    result = []
    for num in int_list:
        if num in pick_me_list:
            result.append(num)
    return result


#  int_list = [1,0,4,0,0,7,7]
def spy_game(int_list):
    picked_numbers = pick((0, 7), int_list)  # returns [0,0,0,7,7]
    found_007 = False
    for i in range(0, len(picked_numbers)-2):
        if picked_numbers[i] == 0 and picked_numbers[i+1] == 0 and picked_numbers[i+2] == 7:
            found_007 = True
            break
    return found_007


print(f'spy_game([1,2,4,0,0,7,5]): {spy_game([1,2,4,0,0,7,5])}')  # True
print(f'spy_game([1,0,2,4,0,5,7]): {spy_game([1,0,2,4,0,5,7])}')  # True
print(f'spy_game([1,7,2,0,4,5,0]): {spy_game([1,7,2,0,4,5,0])}')  # False
print(f'spy_game([1,0,4,0,0,7,7]): {spy_game([1,0,4,0,0,7,7])}')  # True
