

# Refer to unit tests for my_range() function
# NOTE! built-in range is a CLASS implementing __iter__(),  which makes it an iterable.
# Below, we implement a generator function to mimic the behaviour of built in range class
# From range documentation:
# Possible types:
# • (self: range, stop: int) -> None
# • (self: range, start: int, stop: int, step: int) -> None
#
#  range(stop) -> range object range(start, stop[, step]) -> range object
#  Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.
#  range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted!
#  range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements.
#  When step is given, it specifies the increment (or decrement).
def my_range(*args):
    """
    A built-in range() function equivalent, an iterator function
    :param args:  A variable length of arguments
    :return: a generator
    """
    # check if correct number of arguments are given
    if len(args) < 1:
        msg = f'range expected 1 arguments, got {len(args)}'
        raise TypeError(msg)
    if len(args) > 3:
        msg = f'range expected at most 3 arguments, got {len(args)}'
        raise TypeError(msg)

    # number of args is between 1 to 3. Fine.
    # now check the type of args. They all have to be int
    for arg in args:
        if type(arg) != int:
            msg = f'{type(arg)} object cannot be interpreted as an integer'
            raise TypeError(msg)

    # both number of args and type of args are correct
    # start initializing start, stop, step variables
    start = 0
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]

    # start, stop, and step got initialized
    current = start
    while current < stop:
        yield current
        current += step


def gensquares(n):
    """
    a generator that generates the squares of numbers up to some number N.
    :param N:
    :return:
    """
    for number in my_range(n):  # note that we are NOT calling range(N), we implemented our own my_range() generator
        yield number**2


if __name__ == '__main__':
    print('Calling iterator gensquares(10) in a for loop')
    for x in gensquares(10):  # gensquares(10) is a generator throwing StopIteration when exhausted
        print(x)

