# TASK
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections
# of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def is_end_of_list(lst, index):
    return len(lst) <= index


def get_indexes_of(number, int_list):
    """
    i.e. number = 6
         int_list = [1,2,3,6,7,9,5,6,3,9,9,4]
         returns [3,7]
    :param number: the number to find the indexes of in int_list
    :param int_list: a list of integers, which may contain 6s (every 6 is followed by a nine)
    :return: a list containing the indexes of number in int_list
    """

    index = 0
    result = []
    while True:
        if is_end_of_list(int_list, index):
            break
        if number in int_list[index:]:  # if number is found in (the rest of) the int_list
            result.append(index + int_list[index:].index(number))  # result = [3]
            index = result[-1] + 1  # index = 4
            continue
        else:  # cannot find the number in (the rest of) the int_list
            break
    return result  # [3,7]


def get_nine_ranges(six_indexes, length_int_list):
    """
    Given int_list = [1,2,3,6,7,9,5,6,3,9,9,4]
    we have length_int_list = 11
    we have six_indexes = [3,7] (i.e. indexes of value 6 in int_list)
    we have nine_indexes = [5,9,10] (i.e. indexes of value 9 in int_list)
    This function returns result = [(3,(4,6)), (7,(8,11))]
    [4,6] and [8,11] refer to possible index ranges to look for in nine_indexes;
    3 in (3,(4,6)) is 6's index
    7 in (7,(8,11)) is 6's index
    """
    result = []
    for i, six_index in enumerate(six_indexes):  # [(0,3), (1,7)]
        tup = ()
        if (i+1) < len(six_indexes):  # we have not reached the end of six_indexes yet
            tup = (six_index, (six_index+1, six_indexes[i+1]-1))  # (3, (4,6))
        else:  # if we reached the end of six_indexes list
            tup = (six_index, (six_index + 1, length_int_list-1))         # (7,(8,11))
        result.append(tup)
    return result  # [(3,(4,6)), (7,(8,11))]


def get_ignored_sections(nine_ranges, nine_indexes):
    """
    returns a list of tuples. Each tuple contains a starting and a stopping index of
    an ignored section starting with 6's index and ending with 9's index in int_list. The stopping index
    of an ignored section is the minimum nine index that fits into the range
    [min_nine_index, max_nine_index]
    :param nine_ranges: i.e. [(3,(4,6)), (7,(8,11))]
    :param nine_indexes: i.e. [5,9,10]
    :return: i.e. [(3,5),(7,9)]
    """
    ignored_sections = []
    for six_index, (min_nine_index, max_nine_index) in nine_ranges:  # six_index = 3, min_nine_index = 4, max_nine_index = 6
        end_of_ignored_section = 0
        for nine_index in nine_indexes:  # nine_index = 5
            if nine_index < min_nine_index:
                continue
            elif nine_index > max_nine_index:
                break
            else:
                end_of_ignored_section = nine_index  # 5
                break
        tup = (six_index, end_of_ignored_section)  # (3,5)
        ignored_sections.append(tup)               # [(3,5)]
    return ignored_sections                        # [(3,5),(7,9)]


def summer_69(int_list):
    """
    Given int_list = [1,2,3,6,7,9,5,6,3,9,9,4]
    :param int_list: a list of integers, which may contain 6. In case it contains 6, then
    a 9 should follow after the corresponding 6
    :return:
    """
    six_indexes = get_indexes_of(6, int_list)   # [3,7]
    nine_indexes = get_indexes_of(9, int_list)  # [5,9,10]
    nine_ranges = get_nine_ranges(six_indexes, len(int_list))  # [(3,(4,6)), (7,(8,inf))]
    ignored_sections = get_ignored_sections(nine_ranges, nine_indexes)  # [(3,5), (7,9)]
    total = sum(int_list)
    for min_index, max_index in ignored_sections:
        total -= sum(int_list[min_index:max_index+1])
    return total


print(f'summer_69([])): {summer_69([])}')
print(f'summer_69([1, 3, 5])): {summer_69([1, 3, 5])}')
print(f'summer_69([4, 5, 6, 7, 8, 9]): {summer_69([4, 5, 6, 7, 8, 9])}')
print(f'summer_69([2, 1, 6, 9, 11]): {summer_69([2, 1, 6, 9, 11])}')
print(f'summer_69([1, 2, 3, 6, 7, 9, 5, 6, 3, 9, 9, 4]): {summer_69([1, 2, 3, 6, 7, 9, 5, 6, 3, 9, 9, 4])}')
