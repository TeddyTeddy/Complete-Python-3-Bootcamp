
# Refer to unit tests for my_range() function
# NOTE! built-in range is a class implementing __iter__()
# which makes it an iterable. Below, we implement a generator
# function to mimic the behaviour of built in range class
def my_range(N):
    """
    A built-in range() function equivalent, an iterator function
    :param N:  A number to generate the range from [0,N) (i.e. up to but not including N)
    :return: a generator
    """
    lst = []  # start building the ITERABLE
    if N > 0:
        i = 0
        while i < N:
            lst.append(i)
            i += 1

    if lst:  # if it is not an empty iterable lst
        for item in lst:  # looping through the ITERABLE lst
            yield(item)
    else:
        yield lst  # []


def gensquares(N):
    """
    a generator that generates the squares of numbers up to some number N.
    :param N:
    :return:
    """
    for number in my_range(N):  # note that we are NOT calling range(N), we implemented our own my_range() iterator
        yield number**2


if __name__ == '__main__':
    print('Calling iterator gensquares(10) in a for loop')
    for x in gensquares(10):
        print(x)

